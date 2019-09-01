# Created: 8/31/2019
# Author:  Emiliano Jordan,
# Project: WrapPlotLib

from matplotlib import rcParams


class Settings:

    # def __getattribute__(self, item):
    #
    #     private_name = f'_WPL_{item}'
    #
    #     if private_name in self.__dict__:
    #         return super(Settings, self).__getattribute__(private_name)
    #
    #     try:
    #         return super(Settings, self).__getattribute__(item)
    #     except AttributeError:
    #         setattr(self, item, Settings())
    #         return getattr(self, item)

    def __getattr__(self, item):

        setattr(self, item, Settings())
        return getattr(self, item)


settings = Settings()

settings._internal.classic_mode = rcParams['_internal.classic_mode']  # default = False
settings.agg.path.chunksize = rcParams['agg.path.chunksize']  # default = 0
settings.animation.avconv_args = rcParams['animation.avconv_args']  # default = []
settings.animation.avconv_path = rcParams['animation.avconv_path']  # default = 'avconv'
settings.animation.bitrate = rcParams['animation.bitrate']  # default = -1
settings.animation.codec = rcParams['animation.codec']  # default = 'h264'
settings.animation.convert_args = rcParams['animation.convert_args']  # default = []
settings.animation.convert_path = rcParams['animation.convert_path']  # default = 'convert'
settings.animation.embed_limit = rcParams['animation.embed_limit']  # default = 20.0
settings.animation.ffmpeg_args = rcParams['animation.ffmpeg_args']  # default = []
settings.animation.ffmpeg_path = rcParams['animation.ffmpeg_path']  # default = 'ffmpeg'
settings.animation.frame_format = rcParams['animation.frame_format']  # default = 'png'
settings.animation.html = rcParams['animation.html']  # default = 'none'
settings.animation.html_args = rcParams['animation.html_args']  # default = []
settings.animation.writer = rcParams['animation.writer']  # default = 'ffmpeg'
settings.plot.autolimit_mode = rcParams['axes.autolimit_mode']  # default = 'data'
settings.plot.axisbelow = rcParams['axes.axisbelow']  # default = 'line'
settings.plot.edgecolor = rcParams['axes.edgecolor']  # default = 'black'
settings.plot.facecolor = rcParams['axes.facecolor']  # default = 'white'
settings.plot.formatter.limits = rcParams['axes.formatter.limits']  # default = [-7, 7]
settings.plot.formatter.min_exponent = rcParams['axes.formatter.min_exponent']  # default = 0
settings.plot.formatter.offset_threshold = rcParams['axes.formatter.offset_threshold']  # default = 4
settings.plot.formatter.use_locale = rcParams['axes.formatter.use_locale']  # default = False
settings.plot.formatter.use_mathtext = rcParams['axes.formatter.use_mathtext']  # default = False
settings.plot.formatter.useoffset = rcParams['axes.formatter.useoffset']  # default = True
settings.plot.grid.display = rcParams['axes.grid']  # default = False
settings.plot.grid.axis = rcParams['axes.grid.axis']  # default = 'both'
settings.plot.grid.which = rcParams['axes.grid.which']  # default = 'major'
settings.plot.labelcolor = rcParams['axes.labelcolor']  # default = 'black'
settings.plot.labelpad = rcParams['axes.labelpad']  # default = 4.0
settings.plot.labelsize = rcParams['axes.labelsize']  # default = 'medium'
settings.plot.labelweight = rcParams['axes.labelweight']  # default = 'normal'
settings.plot.linewidth = rcParams['axes.linewidth']  # default = 0.8
settings.plot.prop_cycle = rcParams['axes.prop_cycle']  # default = cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
settings.plot.spines.bottom = rcParams['axes.spines.bottom']  # default = True
settings.plot.spines.left = rcParams['axes.spines.left']  # default = True
settings.plot.spines.right = rcParams['axes.spines.right']  # default = True
settings.plot.spines.top = rcParams['axes.spines.top']  # default = True
settings.plot.titlepad = rcParams['axes.titlepad']  # default = 6.0
settings.plot.titlesize = rcParams['axes.titlesize']  # default = 'large'
settings.plot.titleweight = rcParams['axes.titleweight']  # default = 'normal'
settings.plot.unicode_minus = rcParams['axes.unicode_minus']  # default = True
settings.plot.xmargin = rcParams['axes.xmargin']  # default = 0.05
settings.plot.ymargin = rcParams['axes.ymargin']  # default = 0.05
settings.axes3d.grid = rcParams['axes3d.grid']  # default = True
settings.backend.which = rcParams['backend']  # default = 'TkAgg'
settings.backend.qt4 = rcParams['backend.qt4']  # default = None
settings.backend.qt5 = rcParams['backend.qt5']  # default = None
settings.backend_fallback = rcParams['backend_fallback']  # default = True
settings.boxplot.bootstrap = rcParams['boxplot.bootstrap']  # default = None
settings.boxplot.boxprops.color = rcParams['boxplot.boxprops.color']  # default = 'black'
settings.boxplot.boxprops.linestyle = rcParams['boxplot.boxprops.linestyle']  # default = '-'
settings.boxplot.boxprops.linewidth = rcParams['boxplot.boxprops.linewidth']  # default = 1.0
settings.boxplot.capprops.color = rcParams['boxplot.capprops.color']  # default = 'black'
settings.boxplot.capprops.linestyle = rcParams['boxplot.capprops.linestyle']  # default = '-'
settings.boxplot.capprops.linewidth = rcParams['boxplot.capprops.linewidth']  # default = 1.0
settings.boxplot.flierprops.color = rcParams['boxplot.flierprops.color']  # default = 'black'
settings.boxplot.flierprops.linestyle = rcParams['boxplot.flierprops.linestyle']  # default = 'none'
settings.boxplot.flierprops.linewidth = rcParams['boxplot.flierprops.linewidth']  # default = 1.0
settings.boxplot.flierprops.marker = rcParams['boxplot.flierprops.marker']  # default = 'o'
settings.boxplot.flierprops.markeredgecolor = rcParams['boxplot.flierprops.markeredgecolor']  # default = 'black'
settings.boxplot.flierprops.markerfacecolor = rcParams['boxplot.flierprops.markerfacecolor']  # default = 'none'
settings.boxplot.flierprops.markersize = rcParams['boxplot.flierprops.markersize']  # default = 6.0
settings.boxplot.meanline = rcParams['boxplot.meanline']  # default = False
settings.boxplot.meanprops.color = rcParams['boxplot.meanprops.color']  # default = 'C2'
settings.boxplot.meanprops.linestyle = rcParams['boxplot.meanprops.linestyle']  # default = '--'
settings.boxplot.meanprops.linewidth = rcParams['boxplot.meanprops.linewidth']  # default = 1.0
settings.boxplot.meanprops.marker = rcParams['boxplot.meanprops.marker']  # default = '^'
settings.boxplot.meanprops.markeredgecolor = rcParams['boxplot.meanprops.markeredgecolor']  # default = 'C2'
settings.boxplot.meanprops.markerfacecolor = rcParams['boxplot.meanprops.markerfacecolor']  # default = 'C2'
settings.boxplot.meanprops.markersize = rcParams['boxplot.meanprops.markersize']  # default = 6.0
settings.boxplot.medianprops.color = rcParams['boxplot.medianprops.color']  # default = 'C1'
settings.boxplot.medianprops.linestyle = rcParams['boxplot.medianprops.linestyle']  # default = '-'
settings.boxplot.medianprops.linewidth = rcParams['boxplot.medianprops.linewidth']  # default = 1.0
settings.boxplot.notch = rcParams['boxplot.notch']  # default = False
settings.boxplot.patchartist = rcParams['boxplot.patchartist']  # default = False
settings.boxplot.showbox = rcParams['boxplot.showbox']  # default = True
settings.boxplot.showcaps = rcParams['boxplot.showcaps']  # default = True
settings.boxplot.showfliers = rcParams['boxplot.showfliers']  # default = True
settings.boxplot.showmeans = rcParams['boxplot.showmeans']  # default = False
settings.boxplot.vertical = rcParams['boxplot.vertical']  # default = True
settings.boxplot.whiskerprops.color = rcParams['boxplot.whiskerprops.color']  # default = 'black'
settings.boxplot.whiskerprops.linestyle = rcParams['boxplot.whiskerprops.linestyle']  # default = '-'
settings.boxplot.whiskerprops.linewidth = rcParams['boxplot.whiskerprops.linewidth']  # default = 1.0
settings.boxplot.whiskers = rcParams['boxplot.whiskers']  # default = 1.5
settings.contour.corner_mask = rcParams['contour.corner_mask']  # default = True
settings.contour.negative_linestyle = rcParams['contour.negative_linestyle']  # default = 'dashed'
settings.datapath = rcParams['datapath']  # default = 'C:\Users\Volyova\.virtualenvs\WrapPlotLib-4KtjupX6\lib\site-packages\matplotlib\mpl-data'
settings.date.autoformatter.day = rcParams['date.autoformatter.day']  # default = '%Y-%m-%d'
settings.date.autoformatter.hour = rcParams['date.autoformatter.hour']  # default = '%m-%d %H'
settings.date.autoformatter.microsecond = rcParams['date.autoformatter.microsecond']  # default = '%M:%S.%f'
settings.date.autoformatter.minute = rcParams['date.autoformatter.minute']  # default = '%d %H:%M'
settings.date.autoformatter.month = rcParams['date.autoformatter.month']  # default = '%Y-%m'
settings.date.autoformatter.second = rcParams['date.autoformatter.second']  # default = '%H:%M:%S'
settings.date.autoformatter.year = rcParams['date.autoformatter.year']  # default = '%Y'
settings.docstring.hardcopy = rcParams['docstring.hardcopy']  # default = False
settings.errorbar.capsize = rcParams['errorbar.capsize']  # default = 0.0
settings.examples.directory = rcParams['examples.directory']  # default = ''
settings.figure.autolayout = rcParams['figure.autolayout']  # default = False
settings.figure.constrained_layout.h_pad = rcParams['figure.constrained_layout.h_pad']  # default = 0.04167
settings.figure.constrained_layout.hspace = rcParams['figure.constrained_layout.hspace']  # default = 0.02
settings.figure.constrained_layout.use = rcParams['figure.constrained_layout.use']  # default = False
settings.figure.constrained_layout.w_pad = rcParams['figure.constrained_layout.w_pad']  # default = 0.04167
settings.figure.constrained_layout.wspace = rcParams['figure.constrained_layout.wspace']  # default = 0.02
settings.figure.dpi = rcParams['figure.dpi']  # default = 100.0
settings.figure.edgecolor = rcParams['figure.edgecolor']  # default = 'white'
settings.figure.facecolor = rcParams['figure.facecolor']  # default = 'white'
settings.figure.figsize = rcParams['figure.figsize']  # default = [6.4, 4.8]
settings.figure.frameon = rcParams['figure.frameon']  # default = True
settings.figure.max_open_warning = rcParams['figure.max_open_warning']  # default = 20
settings.figure.subplot.bottom = rcParams['figure.subplot.bottom']  # default = 0.11
settings.figure.subplot.hspace = rcParams['figure.subplot.hspace']  # default = 0.2
settings.figure.subplot.left = rcParams['figure.subplot.left']  # default = 0.125
settings.figure.subplot.right = rcParams['figure.subplot.right']  # default = 0.9
settings.figure.subplot.top = rcParams['figure.subplot.top']  # default = 0.88
settings.figure.subplot.wspace = rcParams['figure.subplot.wspace']  # default = 0.2
settings.figure.titlesize = rcParams['figure.titlesize']  # default = 'large'
settings.figure.titleweight = rcParams['figure.titleweight']  # default = 'normal'
settings.font.cursive = rcParams['font.cursive']  # default = ['Apple Chancery', 'Textile', 'Zapf Chancery', 'Sand', 'Script MT', 'Felipa', 'cursive']
settings.font.family = rcParams['font.family']  # default = ['sans-serif']
settings.font.fantasy = rcParams['font.fantasy']  # default = ['Comic Sans MS', 'Chicago', 'Charcoal', 'Impact', 'Western', 'Humor Sans', 'xkcd', 'fantasy']
settings.font.monospace = rcParams['font.monospace']  # default = ['DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Computer Modern Typewriter', 'Andale Mono', 'Nimbus Mono L', 'Courier New', 'Courier', 'Fixed', 'Terminal', 'monospace']
settings.font.sans_serif = rcParams['font.sans-serif']  # default = ['DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', 'sans-serif']
settings.font.serif = rcParams['font.serif']  # default = ['DejaVu Serif', 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook', 'Century Schoolbook L', 'Utopia', 'ITC Bookman', 'Bookman', 'Nimbus Roman No9 L', 'Times New Roman', 'Times', 'Palatino', 'Charter', 'serif']
settings.font.size = rcParams['font.size']  # default = 10.0
settings.font.stretch = rcParams['font.stretch']  # default = 'normal'
settings.font.style = rcParams['font.style']  # default = 'normal'
settings.font.variant = rcParams['font.variant']  # default = 'normal'
settings.font.weight = rcParams['font.weight']  # default = 'normal'
settings.grid.alpha = rcParams['grid.alpha']  # default = 1.0
settings.grid.color = rcParams['grid.color']  # default = '#b0b0b0'
settings.grid.linestyle = rcParams['grid.linestyle']  # default = '-'
settings.grid.linewidth = rcParams['grid.linewidth']  # default = 0.8
settings.hatch.color = rcParams['hatch.color']  # default = 'black'
settings.hatch.linewidth = rcParams['hatch.linewidth']  # default = 1.0
settings.hist.bins = rcParams['hist.bins']  # default = 10
settings.image.aspect = rcParams['image.aspect']  # default = 'equal'
settings.image.cmap = rcParams['image.cmap']  # default = 'viridis'
settings.image.composite_image = rcParams['image.composite_image']  # default = True
settings.image.interpolation = rcParams['image.interpolation']  # default = 'nearest'
settings.image.lut = rcParams['image.lut']  # default = 256
settings.image.origin = rcParams['image.origin']  # default = 'upper'
settings.image.resample = rcParams['image.resample']  # default = True
settings.interactive = rcParams['interactive']  # default = False
settings.keymap.all_axes = rcParams['keymap.all_axes']  # default = ['a']
settings.keymap.back = rcParams['keymap.back']  # default = ['left', 'c', 'backspace']
settings.keymap.copy = rcParams['keymap.copy']  # default = ['ctrl+c', 'cmd+c']
settings.keymap.forward = rcParams['keymap.forward']  # default = ['right', 'v']
settings.keymap.fullscreen = rcParams['keymap.fullscreen']  # default = ['f', 'ctrl+f']
settings.keymap.grid = rcParams['keymap.grid']  # default = ['g']
settings.keymap.grid_minor = rcParams['keymap.grid_minor']  # default = ['G']
settings.keymap.help = rcParams['keymap.help']  # default = ['f1']
settings.keymap.home = rcParams['keymap.home']  # default = ['h', 'r', 'home']
settings.keymap.pan = rcParams['keymap.pan']  # default = ['p']
settings.keymap.quit = rcParams['keymap.quit']  # default = ['ctrl+w', 'cmd+w', 'q']
settings.keymap.quit_all = rcParams['keymap.quit_all']  # default = ['W', 'cmd+W', 'Q']
settings.keymap.save = rcParams['keymap.save']  # default = ['s', 'ctrl+s']
settings.keymap.xscale = rcParams['keymap.xscale']  # default = ['k', 'L']
settings.keymap.yscale = rcParams['keymap.yscale']  # default = ['l']
settings.keymap.zoom = rcParams['keymap.zoom']  # default = ['o']
settings.legend.borderaxespad = rcParams['legend.borderaxespad']  # default = 0.5
settings.legend.borderpad = rcParams['legend.borderpad']  # default = 0.4
settings.legend.columnspacing = rcParams['legend.columnspacing']  # default = 2.0
settings.legend.edgecolor = rcParams['legend.edgecolor']  # default = '0.8'
settings.legend.facecolor = rcParams['legend.facecolor']  # default = 'inherit'
settings.legend.fancybox = rcParams['legend.fancybox']  # default = True
settings.legend.fontsize = rcParams['legend.fontsize']  # default = 'medium'
settings.legend.framealpha = rcParams['legend.framealpha']  # default = 0.8
settings.legend.frameon = rcParams['legend.frameon']  # default = True
settings.legend.handleheight = rcParams['legend.handleheight']  # default = 0.7
settings.legend.handlelength = rcParams['legend.handlelength']  # default = 2.0
settings.legend.handletextpad = rcParams['legend.handletextpad']  # default = 0.8
settings.legend.labelspacing = rcParams['legend.labelspacing']  # default = 0.5
settings.legend.loc = rcParams['legend.loc']  # default = 'best'
settings.legend.markerscale = rcParams['legend.markerscale']  # default = 1.0
settings.legend.numpoints = rcParams['legend.numpoints']  # default = 1
settings.legend.scatterpoints = rcParams['legend.scatterpoints']  # default = 1
settings.legend.shadow = rcParams['legend.shadow']  # default = False
settings.legend.title_fontsize = rcParams['legend.title_fontsize']  # default = None
settings.lines.antialiased = rcParams['lines.antialiased']  # default = True
settings.lines.color = rcParams['lines.color']  # default = 'C0'
settings.lines.dash_capstyle = rcParams['lines.dash_capstyle']  # default = 'butt'
settings.lines.dash_joinstyle = rcParams['lines.dash_joinstyle']  # default = 'round'
settings.lines.dashdot_pattern = rcParams['lines.dashdot_pattern']  # default = [6.4, 1.6, 1.0, 1.6]
settings.lines.dashed_pattern = rcParams['lines.dashed_pattern']  # default = [3.7, 1.6]
settings.lines.dotted_pattern = rcParams['lines.dotted_pattern']  # default = [1.0, 1.65]
settings.lines.linestyle = rcParams['lines.linestyle']  # default = '-'
settings.lines.linewidth = rcParams['lines.linewidth']  # default = 1.5
settings.lines.marker = rcParams['lines.marker']  # default = 'None'
settings.lines.markeredgecolor = rcParams['lines.markeredgecolor']  # default = 'auto'
settings.lines.markeredgewidth = rcParams['lines.markeredgewidth']  # default = 1.0
settings.lines.markerfacecolor = rcParams['lines.markerfacecolor']  # default = 'auto'
settings.lines.markersize = rcParams['lines.markersize']  # default = 6.0
settings.lines.scale_dashes = rcParams['lines.scale_dashes']  # default = True
settings.lines.solid_capstyle = rcParams['lines.solid_capstyle']  # default = 'projecting'
settings.lines.solid_joinstyle = rcParams['lines.solid_joinstyle']  # default = 'round'
settings.markers.fillstyle = rcParams['markers.fillstyle']  # default = 'full'
settings.mathtext.bf = rcParams['mathtext.bf']  # default = 'sans:bold'
settings.mathtext.cal = rcParams['mathtext.cal']  # default = 'cursive'
settings.mathtext.default = rcParams['mathtext.default']  # default = 'it'
settings.mathtext.fallback_to_cm = rcParams['mathtext.fallback_to_cm']  # default = True
settings.mathtext.fontset = rcParams['mathtext.fontset']  # default = 'dejavusans'
settings.mathtext.it = rcParams['mathtext.it']  # default = 'sans:italic'
settings.mathtext.rm = rcParams['mathtext.rm']  # default = 'sans'
settings.mathtext.sf = rcParams['mathtext.sf']  # default = 'sans'
settings.mathtext.tt = rcParams['mathtext.tt']  # default = 'monospace'
settings.patch.antialiased = rcParams['patch.antialiased']  # default = True
settings.patch.edgecolor = rcParams['patch.edgecolor']  # default = 'black'
settings.patch.facecolor = rcParams['patch.facecolor']  # default = 'C0'
settings.patch.force_edgecolor = rcParams['patch.force_edgecolor']  # default = False
settings.patch.linewidth = rcParams['patch.linewidth']  # default = 1.0
settings.path.effects = rcParams['path.effects']  # default = []
settings.path.simplify = rcParams['path.simplify']  # default = True
settings.path.simplify_threshold = rcParams['path.simplify_threshold']  # default = 0.1111111111111111
settings.path.sketch = rcParams['path.sketch']  # default = None
settings.path.snap = rcParams['path.snap']  # default = True
settings.pdf.compression = rcParams['pdf.compression']  # default = 6
settings.pdf.fonttype = rcParams['pdf.fonttype']  # default = 3
settings.pdf.inheritcolor = rcParams['pdf.inheritcolor']  # default = False
settings.pdf.use14corefonts = rcParams['pdf.use14corefonts']  # default = False
settings.pgf.preamble = rcParams['pgf.preamble']  # default = []
settings.pgf.rcfonts = rcParams['pgf.rcfonts']  # default = True
settings.pgf.texsystem = rcParams['pgf.texsystem']  # default = 'xelatex'
settings.polaraxes.grid = rcParams['polaraxes.grid']  # default = True
settings.ps.distiller.res = rcParams['ps.distiller.res']  # default = 6000
settings.ps.fonttype = rcParams['ps.fonttype']  # default = 3
settings.ps.papersize = rcParams['ps.papersize']  # default = 'letter'
settings.ps.useafm = rcParams['ps.useafm']  # default = False
settings.ps.usedistiller = rcParams['ps.usedistiller']  # default = False
settings.savefig.bbox = rcParams['savefig.bbox']  # default = None
settings.savefig.directory = rcParams['savefig.directory']  # default = '~'
settings.savefig.dpi = rcParams['savefig.dpi']  # default = 'figure'
settings.savefig.edgecolor = rcParams['savefig.edgecolor']  # default = 'white'
settings.savefig.facecolor = rcParams['savefig.facecolor']  # default = 'white'
settings.savefig.format = rcParams['savefig.format']  # default = 'png'
settings.savefig.frameon = rcParams['savefig.frameon']  # default = True
settings.savefig.jpeg_quality = rcParams['savefig.jpeg_quality']  # default = 95
settings.savefig.orientation = rcParams['savefig.orientation']  # default = 'portrait'
settings.savefig.pad_inches = rcParams['savefig.pad_inches']  # default = 0.1
settings.savefig.transparent = rcParams['savefig.transparent']  # default = False
settings.scatter.marker = rcParams['scatter.marker']  # default = 'o'
settings.svg.fonttype = rcParams['svg.fonttype']  # default = 'path'
settings.svg.hashsalt = rcParams['svg.hashsalt']  # default = None
settings.svg.image_inline = rcParams['svg.image_inline']  # default = True
settings.text.antialiased = rcParams['text.antialiased']  # default = True
settings.text.color = rcParams['text.color']  # default = 'black'
settings.text.hinting = rcParams['text.hinting']  # default = 'auto'
settings.text.hinting_factor = rcParams['text.hinting_factor']  # default = 8
settings.text.latex.preamble = rcParams['text.latex.preamble']  # default = []
settings.text.latex.preview = rcParams['text.latex.preview']  # default = False
settings.text.latex.unicode = rcParams['text.latex.unicode']  # default = True
settings.text.usetex = rcParams['text.usetex']  # default = False
settings.timezone = rcParams['timezone']  # default = 'UTC'
settings.tk.window_focus = rcParams['tk.window_focus']  # default = False
settings.toolbar = rcParams['toolbar']  # default = 'toolbar2'
settings.verbose.fileo = rcParams['verbose.fileo']  # default = 'sys.stdout'
settings.verbose.level = rcParams['verbose.level']  # default = 'silent'
settings.webagg.address = rcParams['webagg.address']  # default = '127.0.0.1'
settings.webagg.open_in_browser = rcParams['webagg.open_in_browser']  # default = True
settings.webagg.port = rcParams['webagg.port']  # default = 8988
settings.webagg.port_retries = rcParams['webagg.port_retries']  # default = 50
settings.xtick.alignment = rcParams['xtick.alignment']  # default = 'center'
settings.xtick.bottom = rcParams['xtick.bottom']  # default = True
settings.xtick.color = rcParams['xtick.color']  # default = 'black'
settings.xtick.direction = rcParams['xtick.direction']  # default = 'out'
settings.xtick.labelbottom = rcParams['xtick.labelbottom']  # default = True
settings.xtick.labelsize = rcParams['xtick.labelsize']  # default = 'medium'
settings.xtick.labeltop = rcParams['xtick.labeltop']  # default = False
settings.xtick.major.bottom = rcParams['xtick.major.bottom']  # default = True
settings.xtick.major.pad = rcParams['xtick.major.pad']  # default = 3.5
settings.xtick.major.size = rcParams['xtick.major.size']  # default = 3.5
settings.xtick.major.top = rcParams['xtick.major.top']  # default = True
settings.xtick.major.width = rcParams['xtick.major.width']  # default = 0.8
settings.xtick.minor.bottom = rcParams['xtick.minor.bottom']  # default = True
settings.xtick.minor.pad = rcParams['xtick.minor.pad']  # default = 3.4
settings.xtick.minor.size = rcParams['xtick.minor.size']  # default = 2.0
settings.xtick.minor.top = rcParams['xtick.minor.top']  # default = True
settings.xtick.minor.visible = rcParams['xtick.minor.visible']  # default = False
settings.xtick.minor.width = rcParams['xtick.minor.width']  # default = 0.6
settings.xtick.top = rcParams['xtick.top']  # default = False
settings.ytick.alignment = rcParams['ytick.alignment']  # default = 'center_baseline'
settings.ytick.color = rcParams['ytick.color']  # default = 'black'
settings.ytick.direction = rcParams['ytick.direction']  # default = 'out'
settings.ytick.labelleft = rcParams['ytick.labelleft']  # default = True
settings.ytick.labelright = rcParams['ytick.labelright']  # default = False
settings.ytick.labelsize = rcParams['ytick.labelsize']  # default = 'medium'
settings.ytick.left = rcParams['ytick.left']  # default = True
settings.ytick.major.left = rcParams['ytick.major.left']  # default = True
settings.ytick.major.pad = rcParams['ytick.major.pad']  # default = 3.5
settings.ytick.major.right = rcParams['ytick.major.right']  # default = True
settings.ytick.major.size = rcParams['ytick.major.size']  # default = 3.5
settings.ytick.major.width = rcParams['ytick.major.width']  # default = 0.8
settings.ytick.minor.left = rcParams['ytick.minor.left']  # default = True
settings.ytick.minor.pad = rcParams['ytick.minor.pad']  # default = 3.4
settings.ytick.minor.right = rcParams['ytick.minor.right']  # default = True
settings.ytick.minor.size = rcParams['ytick.minor.size']  # default = 2.0
settings.ytick.minor.visible = rcParams['ytick.minor.visible']  # default = False
settings.ytick.minor.width = rcParams['ytick.minor.width']  # default = 0.6
settings.ytick.right = rcParams['ytick.right']  # default = False
