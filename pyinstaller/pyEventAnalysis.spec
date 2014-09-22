# -*- mode: python -*-
import sys
import glob
from utilities.resource_path import resource_path, format_path

a = Analysis([format_path('../qtgui/qtAnalysisGUI.py')],
		pathex=[resource_path(".settings")],
		hiddenimports=['scipy.special._ufuncs_cxx', 'qtgui.mplwidget'],
		hookspath=None,
		runtime_hooks=None)
a.datas += [('.settings', format_path('../.settings'), 'DATA')]
pyz = PYZ(a.pure)

# On OS X, collect data files and  build an application bundle
if sys.platform=='darwin':
	exe = EXE(pyz,
		a.scripts,
		name='pyEventAnalysis',
		debug=False,
		strip=None,
		upx=True,
		console=False )
	coll = COLLECT(exe,
		a.binaries,
		Tree('../qtgui/ui', prefix='ui'),
		a.zipfiles,
		a.datas,
		strip=None,
		upx=True,
		name=os.path.join('dist', 'pyEventAnalysis'))
	app = BUNDLE(coll,
		name=os.path.join('dist', 'pyEventAnalysis.app'))
elif sys.platform=='win32' or sys.platform=='win64':
	for d in a.datas:
		if 'pyconfig' in d[0]: 
			a.datas.remove(d)
			break
	exe = EXE(pyz,
		a.scripts,
		# a.binaries,
		# Tree(format_path('../qtgui/ui'), prefix='ui'),
		# a.zipfiles,
		# a.datas,
		name='pyEventAnalysis.exe',
		debug=False,
		strip=None,
		upx=True, 
		exclude_binaries=True,
		console=True )
	coll = COLLECT(exe,
		a.binaries,
		Tree(format_path('../qtgui/ui'), prefix='ui'),
		a.zipfiles,
		a.datas,
		strip=None,
		upx=True,
		name=os.path.join('dist', 'pyEventAnalysis'))