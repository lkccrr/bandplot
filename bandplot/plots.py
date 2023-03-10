import matplotlib.pyplot as plt

# bandplot

def Noneispin(EXPORT, figsize, vertical, arr, bands, ticks, labels, linestyle, linewidth, legend, location, color):
    plt.figure(figsize=figsize)
    if len(color) == 0:
        color = ['r']

    plt.plot(arr, bands.T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    plt.tick_params(axis='y', which='minor', color='gray')

    plt.axhline(linewidth=0.4, linestyle='-.', c='gray')
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            plt.axvline(i, linewidth=0.4, linestyle='-.', c='gray')

    plt.xticks(ticks,labels)
    plt.legend(legend, frameon=False, prop={'size':'medium'}, loc=location)
    plt.xlim(arr[0], arr[-1])
    plt.ylim(vertical)
    plt.ylabel('Energy (eV)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def Ispin(EXPORT, figsize, vertical, arr, bands, ticks, labels, linestyle, linewidth, legend, location, color):
    plt.figure(figsize=figsize)
    if len(color) == 0:
        color = ['r', 'k']
    elif len(color) == 1:
        color = [color[0], 'k']

    if len(linestyle) == 1:
        linestyle = [linestyle[0], '-.']

    if len(linewidth) == 1:
        linewidth = [linewidth[0], 0.8]

    p_up = plt.plot(arr, bands[0].T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    p_do = plt.plot(arr, bands[1].T, color=color[1], linewidth=linewidth[1], linestyle=linestyle[1])
    plt.legend([p_up[0], p_do[0]], ['up', 'down'], frameon=False, prop={'style':'italic', 'size':'medium'}, alignment='left', loc=location, title=legend[0], title_fontproperties={'size':'medium'})
    plt.tick_params(axis='y', which='minor', color='gray')
    plt.axhline(linewidth=0.4, linestyle='-.', c='gray')
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            plt.axvline(i, linewidth=0.4, linestyle='-.', c='gray')

    plt.xlim(arr[0], arr[-1])
    plt.ylim(vertical)
    plt.xticks(ticks,labels)
    plt.ylabel('Energy (eV)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def Dispin(EXPORT, figsize, vertical, arr, bands, ticks, labels, linestyle, linewidth, legend, location, color):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    fig.subplots_adjust(wspace=0.0)
    if len(color) == 0:
        color = ['r', 'k']
    elif len(color) == 1:
        color = [color[0], 'k']

    if len(linestyle) == 1:
        linestyle = [linestyle[0], '-.']

    if len(linewidth) == 1:
        linewidth = [linewidth[0], 0.8]

    ax1.plot(arr, bands[0].T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    ax2.plot(arr, bands[1].T, color=color[1], linewidth=linewidth[1], linestyle=linestyle[1])
    ax1.legend(['up'], frameon=False, prop={'style':'italic', 'size':'medium'}, alignment='left', loc=location, title=legend[0], title_fontproperties={'size':'medium'})
    ax2.legend(['down'], frameon=False, prop={'style':'italic', 'size':'medium'}, alignment='left', loc=location)
    ax1.tick_params(axis='y', which='minor', color='gray')
    ax2.tick_params(axis='y', which='minor', color='gray')

    ax1.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.set_yticklabels([])
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i, linewidth=0.4, linestyle='-.', c='gray')
            ax2.axvline(i, linewidth=0.4, linestyle='-.', c='gray')

    ax1.set_xlim(arr[0], arr[-1])
    ax1.set_ylim(vertical)
    ax2.set_xlim(arr[0], arr[-1])
    ax2.set_ylim(vertical)
    ax1.set_xticks(ticks,labels[:-1]+[''])
    ax2.set_xticks(ticks,labels)
    ax1.set_ylabel('Energy (eV)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def NoneispinWd(EXPORT, figsize, vertical, horizontal, arr, bands, ticks, labels, darr, dele, fill, index_f, elements, width_ratios, linestyle, linewidth, legend, location, color):
    fig, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[1-width_ratios, width_ratios], figsize=figsize)
    fig.subplots_adjust(wspace=0.0)
    if len(color) == 0:
        color = ['r']

    ax1.plot(arr, bands.T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    num = len(index_f)
    p_dos = []
    if num + 1 > len(color):
        color = color + [''] * (num + 1 - len(color))

    if num + 1 > len(linestyle):
        linestyle = linestyle + ['-'] * (num + 1 - len(linestyle))

    if num + 1 > len(linewidth):
        linewidth = linewidth + [0.8] * (num + 1 - len(linewidth))

    for i in range(num):
        if color[i+1]:
            ax2.plot(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], linewidth=linewidth[i+1], linestyle=linestyle[i+1], color=color[i+1])
            if fill:
                plt.fill_between(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], 0, color=color[i+2], alpha=0.2)
        else:
            ax2.plot(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], linewidth=linewidth[i+1], linestyle=linestyle[i+1])
            if fill:
                plt.fill_between(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], 0, alpha=0.2)

    ax1.legend(legend, frameon=False, prop={'size':'small'}, loc=location)
    ax1.tick_params(axis='y', which='minor', color='gray')
    ax2.minorticks_on()
    ax2.tick_params(axis='both', which='minor', color='gray')
    ax2.set_yticklabels([])
    ax2.legend(p_dos, elements, frameon=False, prop={'size':'small'}, alignment='left', loc=location, title="Density of states", title_fontproperties={'size':'small'})
    ax1.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.axvline(linewidth=0.4, linestyle='-.', c='gray')
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i,linewidth=0.4,linestyle='-.',c='gray')

    ax1.set_xlim(arr[0], arr[-1])
    ax1.set_ylim(vertical)
    ax2.set_xlim(horizontal)
    ax2.set_ylim(vertical)
    ax1.set_xticks(ticks,labels)
    ax2.tick_params(axis='x', labelsize='x-small', labelcolor='dimgray', labelrotation=-90, pad=1.5)
    ax1.set_ylabel('Energy (eV)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def IspinWd(EXPORT, figsize, vertical, horizontal, arr, bands, ticks, labels, darr, dele, fill, index_f, elements, width_ratios, linestyle, linewidth, legend, location, color):
    fig, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[1-width_ratios, width_ratios], figsize=figsize)
    fig.subplots_adjust(wspace=0.0)
    if len(color) == 0:
        color = ['r', 'k']
    elif len(color) == 1:
        color = [color[0], 'k']

    if len(linestyle) == 1:
        linestyle = [linestyle[0], '-.']

    if len(linewidth) == 1:
        linewidth = [linewidth[0], 0.8]

    p_up = ax1.plot(arr, bands[0].T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    p_do = ax1.plot(arr, bands[1].T, color=color[1], linewidth=linewidth[1], linestyle=linestyle[1])
    ax1.legend([p_up[0], p_do[0]], ['up', 'down'], frameon=False, prop={'style':'italic', 'size':'small'}, alignment='left', loc=location, title=legend[0], title_fontproperties={'size':'small'})
    num = len(index_f)
    p_dos = []
    if num + 2 > len(color):
        color = color + [''] * (num + 2 - len(color))

    if num + 2 > len(linestyle):
        linestyle = linestyle + ['-'] * (num + 2 - len(linestyle))

    if num + 2 > len(linewidth):
        linewidth = linewidth + [0.8] * (num + 2 - len(linewidth))

    for i in range(num):
        if color[i+2]:
            p_dos = p_dos + ax2.plot(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], linewidth=linewidth[i+2], linestyle=linestyle[i+2], color=color[i+2])
            if fill:
                plt.fill_between(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], 0, color=color[i+2], alpha=0.2)
        else:
            p_dos = p_dos + ax2.plot(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], linewidth=linewidth[i+2], linestyle=linestyle[i+2])
            if fill:
                plt.fill_between(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], 0, alpha=0.2)

    ax1.tick_params(axis='y', which='minor', color='gray')
    ax2.minorticks_on()
    ax2.tick_params(axis='both', which='minor', color='gray')
    ax2.axvline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.set_yticklabels([])
    ax2.legend(p_dos, elements, frameon=False, prop={'size':'small'}, alignment='left', loc=location, title="Density of states", title_fontproperties={'size':'small'})
    ax1.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.axhline(linewidth=0.4, linestyle='-.', c='gray')
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i,linewidth=0.4, linestyle='-.', c='gray')

    ax1.set_xlim(arr[0], arr[-1])
    ax1.set_ylim(vertical)
    ax2.set_xlim(horizontal)
    ax2.set_ylim(vertical)
    ax1.set_xticks(ticks,labels)
    ax2.tick_params(axis='x', labelsize='x-small', labelcolor='dimgray', labelrotation=-90, pad=1.5)
    ax1.set_ylabel('Energy (eV)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def DispinWd(EXPORT, figsize, vertical, horizontal, arr, bands, ticks, labels, darr, dele, fill, index_f, elements, width_ratios, linestyle, linewidth, legend, location, color):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, width_ratios=[0.4*(1-width_ratios), 0.4*(1-width_ratios), width_ratios], figsize=figsize)
    fig.subplots_adjust(wspace=0.0)
    if len(color) == 0:
        color = ['r', 'k']
    elif len(color) == 1:
        color = [color[0], 'k']

    if len(linestyle) == 1:
        linestyle = [linestyle[0], '-.']

    if len(linewidth) == 1:
        linewidth = [linewidth[0], 0.8]

    ax1.plot(arr, bands[0].T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    ax2.plot(arr, bands[1].T, color=color[1], linewidth=linewidth[1], linestyle=linestyle[1])
    ax1.legend(['up'], frameon=False, prop={'style':'italic', 'size':'small'}, alignment='left', loc=location, title=legend[0], title_fontproperties={'size':'small'})
    ax2.legend(['down'], frameon=False, prop={'style':'italic', 'size':'small'}, alignment='left', loc=location)
    ax1.tick_params(axis='y', which='minor', color='gray')
    ax2.tick_params(axis='y', which='minor', color='gray')
    ax3.minorticks_on()
    ax3.tick_params(axis='both', which='minor', color='gray')
    num = len(index_f)
    p_dos = []
    if num + 2 > len(color):
        color = color + [''] * (num + 2 - len(color))

    if num + 2 > len(linestyle):
        linestyle = linestyle + ['-'] * (num + 2 - len(linestyle))

    if num + 2 > len(linewidth):
        linewidth = linewidth + [0.8] * (num + 2 - len(linewidth))

    for i in range(num):
        if color[i+2]:
            p_dos = p_dos + ax3.plot(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], linewidth=linewidth[i+2], linestyle=linestyle[i+2], color=color[i+2])
            if fill:
                plt.fill_between(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], 0, color=color[i+2], alpha=0.2)
        else:
            p_dos = p_dos + ax3.plot(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], linewidth=linewidth[i+2], linestyle=linestyle[i+2])
            if fill:
                plt.fill_between(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], 0, alpha=0.2)

    ax3.axvline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.set_yticklabels([])
    ax3.set_yticklabels([])
    ax3.legend(p_dos, elements, frameon=False, prop={'size':'small'}, alignment='left', loc=location, title="Density of states", title_fontproperties={'size':'small'})

    ax1.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax3.axhline(linewidth=0.4, linestyle='-.', c='gray')
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i,linewidth=0.4,linestyle='-.',c='gray')
            ax2.axvline(i,linewidth=0.4,linestyle='-.',c='gray')

    ax1.set_xlim(arr[0], arr[-1])
    ax1.set_ylim(vertical)
    ax2.set_xlim(arr[0], arr[-1])
    ax2.set_ylim(vertical)
    ax3.set_xlim(horizontal)
    ax3.set_ylim(vertical)
    ax1.set_xticks(ticks,labels[:-1]+[''])
    ax2.set_xticks(ticks,labels)
    ax3.tick_params(axis='x', labelsize='x-small', labelcolor='dimgray', labelrotation=-90, pad=1.5)
    ax1.set_ylabel('Energy (eV)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def pdosfiles(EXPORT, figsize, vertical, horizontal, darr, dele, fill, index_f, elements, linestyle, linewidth, legend, location, exchange, color):
    plt.figure(figsize=figsize)
    plt.minorticks_on()
    plt.tick_params(axis='both', which='minor', color='gray')
    num = len(index_f)
    p_dos = []
    if num > len(color):
        color = color + [''] * (num - len(color))

    if num > len(linestyle):
        linestyle = linestyle + ['-'] * (num - len(linestyle))

    if num > len(linewidth):
        linewidth = linewidth + [0.8] * (num - len(linewidth))

    if exchange:
        for i in range(num):
            if color[i]:
                p_dos = p_dos + plt.plot(darr[index_f[i][0]], dele[index_f[i][0]].T[index_f[i][1]], linewidth=linewidth[i], linestyle=linestyle[i], color=color[i])
                if fill:
                    plt.fill_between(darr[index_f[i][0]], dele[index_f[i][0]].T[index_f[i][1]], 0, color=color[i], alpha=0.2)
            else:
                p_dos = p_dos + plt.plot(darr[index_f[i][0]], dele[index_f[i][0]].T[index_f[i][1]], linewidth=linewidth[i], linestyle=linestyle[i])
                if fill:
                    plt.fill_between(darr[index_f[i][0]], dele[index_f[i][0]].T[index_f[i][1]], 0, alpha=0.2)

        plt.tick_params(axis='y', labelsize='medium', labelcolor='dimgray')
        plt.xlim(vertical)
        plt.ylim(horizontal)
        plt.xlabel('Energy (eV)')
        plt.ylabel('Density of states, electrons/eV')
    else:
        for i in range(num):
            if color[i]:
                p_dos = p_dos + plt.plot(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], linewidth=0.8, linestyle=linestyle[i], color=color[i])
                if fill:
                    plt.fill_between(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], 0, color=color[i], alpha=0.2)
            else:
                p_dos = p_dos + plt.plot(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], linewidth=0.8, linestyle=linestyle[i])
                if fill:
                    plt.fill_between(dele[index_f[i][0]].T[index_f[i][1]], darr[index_f[i][0]], 0, alpha=0.2)

        plt.tick_params(axis='x', labelsize='medium', labelcolor='dimgray')
        plt.ylim(vertical)
        plt.xlim(horizontal)
        plt.ylabel('Energy (eV)')
        plt.xlabel('Density of states, electrons/eV')

    plt.axvline(linewidth=0.4, linestyle='-.', c='gray')
    plt.axhline(linewidth=0.4, linestyle='-.', c='gray')
    plt.legend(p_dos, elements, frameon=False, prop={'size':'medium'}, loc=location, title=legend[0], title_fontproperties={'size':'medium'})
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

# pbandplot

def Broken(EXPORT,  figsize, vertical, arr, fre, ticks, labels, broken, height_ratio, linestyle, linewidth, legend, location, color):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, height_ratios=[height_ratio, 1-height_ratio], figsize=figsize)
    fig.subplots_adjust(hspace=0.0)
    if len(color) == 0:
        color = ['r']

    ax1.plot(arr, fre.T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    ax2.plot(arr, fre.T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    plt.xlim(arr[0], arr[-1])
    if vertical is None:
        vertical = plt.ylim()

    ax1.set_ylim(broken[1], vertical[1])
    ax2.set_ylim(vertical[0], broken[0])
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position(position='none')
    ax1.tick_params(axis='y', which='minor', color='darkgray')
    ax1.tick_params(axis='y', labelsize='small', labelcolor='dimgray', labelrotation=-60)
    ax2.tick_params(axis='y', which='minor', color='gray')
    ax2.axhline(linewidth=0.4, linestyle='-.', c='gray')
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i, linewidth=0.4, linestyle='-.', c='gray')
            ax2.axvline(i, linewidth=0.4, linestyle='-.', c='gray')

    ax2.legend(legend, frameon=False, prop={'size':'medium'}, loc=location)
    plt.xticks(ticks,labels)
    plt.suptitle('Frequency (THz)', rotation=90, x=0.06, y=0.6, size='medium')
    kwargs = dict(marker=[(-1, -1), (1, 1)], markersize=6,
                  linestyle='', color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0.02, 0.02], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [0.98, 0.98], transform=ax2.transAxes, **kwargs)
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def Nobroken(EXPORT, figsize, vertical, arr, fre, ticks, labels, linestyle, linewidth, legend, location, color):
    plt.figure(figsize=figsize)
    if len(color) == 0:
        color = ['r']

    plt.plot(arr, fre.T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    plt.tick_params(axis='y', which='minor', color='gray')
    plt.axhline(linewidth=0.4, linestyle='-.', c='gray')
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            plt.axvline(i, linewidth=0.4, linestyle='-.', c='gray')

    plt.legend(legend, frameon=False, prop={'size':'medium'}, loc=location)
    plt.xticks(ticks,labels)
    plt.xlim(arr[0], arr[-1])
    plt.ylim(vertical)
    plt.ylabel('Frequency (THz)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def BrokenWd(EXPORT, figsize, vertical, horizontal, arr, fre, ticks, labels, broken, height_ratio, darr, dele, fill, elements, width_ratios, linestyle, linewidth, legend, location, color):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, height_ratios=[height_ratio, 1-height_ratio], width_ratios=[1-width_ratios, width_ratios], figsize=figsize)
    fig.subplots_adjust(wspace=0.0, hspace=0.0)
    if len(color) == 0:
        color = ['r']

    ax1.plot(arr, fre.T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    ax3.plot(arr, fre.T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    num = dele.shape[-1]
    p_dos = []
    if num + 1 > len(color):
        color = color + [''] * (num - len(color) + 1)

    if num + 1 > len(linestyle):
        linestyle = linestyle + ['-'] * (num - len(linestyle) + 1)

    if num + 1 > len(linewidth):
        linewidth = linewidth + [0.8] * (num - len(linewidth) + 1)

    for i in range(num):
        if color[i+1]:
            ax2.plot(dele[:,i], darr, linewidth=linewidth[i+1], linestyle=linestyle[i+1], color=color[i+1])
            p_dos = p_dos + ax4.plot(dele[:,i], darr, linewidth=linewidth[i+1], linestyle=linestyle[i+1], color=color[i+1])
            if fill:
                plt.fill_between(dele[:,i], darr, 0, color=color[i], alpha=0.2)
        else:
            ax2.plot(dele[:,i], darr, linewidth=linewidth[i+1], linestyle=linestyle[i+1])
            p_dos = p_dos + ax4.plot(dele[:,i], darr, linewidth=linewidth[i+1], linestyle=linestyle[i+1])
            if fill:
                plt.fill_between(dele[:,i], darr, 0, alpha=0.2)

    ax1.set_xlim(arr[0], arr[-1])
    ax3.set_xlim(arr[0], arr[-1])
    if vertical is None:
        vertical = ax1.get_ylim()

    ax1.set_ylim(broken[1], vertical[1])
    ax2.set_ylim(broken[1], vertical[1])
    ax3.set_ylim(vertical[0], broken[0])
    ax4.set_ylim(vertical[0], broken[0])
    ax2.set_xlim(horizontal)
    ax4.set_xlim(horizontal)
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax3.spines['top'].set_visible(False)
    ax4.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position('none')
    ax2.xaxis.set_ticks_position('none')
    ax1.tick_params(axis='y', which='minor', color='darkgray')
    ax1.tick_params(axis='y', labelsize='small', labelcolor='dimgray', labelrotation=-60)
    ax3.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax4.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.tick_params(axis='y', which='minor', color='darkgray')
    ax3.tick_params(axis='y', which='minor', color='gray')
    ax4.minorticks_on()
    ax4.tick_params(axis='x', labelsize='small', labelcolor='dimgray', labelrotation=-90, pad=3)
    ax4.tick_params(axis='both', which='minor', color='gray')
    ax1.set_xticklabels([])
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax4.set_yticklabels([])
    ax2.axvline(linewidth=0.4, linestyle='-.', c='gray')
    ax4.axvline(linewidth=0.4, linestyle='-.', c='gray')
    if num > len(elements):
        elements = elements + [''] * (num - len(elements))
    elif num < len(elements):
        if num == 1:
            elements = ['$tdos$']
        else:
            elements = elements[:num]

    ax3.legend(legend, frameon=False, prop={'size':'small'}, loc=location)
    ax4.legend(p_dos, elements, frameon=False, prop={'size':'small'}, alignment='left', loc=location, title="Phonon DOS", title_fontproperties={'size':'small'})
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i, linewidth=0.4, linestyle='-.', c='gray')
            ax3.axvline(i, linewidth=0.4, linestyle='-.', c='gray')

    ax3.set_xticks(ticks,labels)
    plt.suptitle('Frequency (THz)', rotation=90, x=0.06, y=0.6, size='medium')
    kwargs = dict(marker=[(-1, -1), (1, 1)], markersize=6,
                  linestyle='', color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0.02, 0.02], transform=ax1.transAxes, **kwargs)
    ax3.plot([0, 1], [0.98, 0.98], transform=ax3.transAxes, **kwargs)
    ax2.plot(1, 0.02, transform=ax2.transAxes, **kwargs)
    ax4.plot(1, 0.98, transform=ax4.transAxes, **kwargs)
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def NobrokenWd(EXPORT, figsize, vertical, horizontal, arr, fre, ticks, labels, darr, dele, fill, elements, width_ratios, linestyle, linewidth, legend, location, color):
    fig, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[1-width_ratios, width_ratios], figsize=figsize)
    fig.subplots_adjust(wspace=0.0)
    if len(color) == 0:
        color = ['r']

    ax1.plot(arr, fre.T, color=color[0], linewidth=linewidth[0], linestyle=linestyle[0])
    num = dele.shape[-1]
    p_dos = []
    if num + 1 > len(color):
        color = color + [''] * (num - len(color) + 1)

    if num + 1 > len(linestyle):
        linestyle = linestyle + ['-'] * (num - len(linestyle) + 1)

    if num + 1 > len(linewidth):
        linewidth = linewidth + [0.8] * (num - len(linewidth) + 1)

    for i in range(num):
        if color[i+1]:
            p_dos = p_dos + ax2.plot(dele[:,i], darr, linewidth=linewidth[i+1], linestyle=linestyle[i+1], color=color[i+1])
            if fill:
                plt.fill_between(dele[:,i], darr, 0, color=color[i], alpha=0.2)
        else:
            p_dos = p_dos + ax2.plot(dele[:,i], darr, linewidth=linewidth[i+1], linestyle=linestyle[i+1])
            if fill:
                plt.fill_between(dele[:,i], darr, 0, alpha=0.2)

    ax1.set_xlim(arr[0], arr[-1])
    if vertical is None:
        vertical = ax1.get_ylim()

    ax1.set_ylim(vertical)
    ax2.set_ylim(vertical)
    ax2.set_xlim(horizontal)
    ax1.tick_params(axis='y', which='minor', color='gray')
    ax1.axhline(linewidth=0.4, linestyle='-.', c='gray')
    ax2.minorticks_on()
    ax2.tick_params(axis='x', labelsize='small', labelcolor='dimgray', labelrotation=-90, pad=3)
    ax2.tick_params(axis='both', which='minor', color='gray')
    ax2.set_yticklabels([])
    ax2.axhline(linewidth=0.4, linestyle='-.', c='gray')
    if num > len(elements):
        elements = elements + [''] * (num - len(elements))
    elif num < len(elements):
        if num == 1:
            elements = ['$tdos$']
        else:
            elements = elements[:num]

    ax1.legend(legend, frameon=False, prop={'size':'small'}, loc=location)
    ax2.axvline(linewidth=0.4,linestyle='-.',c='dimgray')
    ax2.legend(p_dos, elements, frameon=False, prop={'size':'small'}, alignment='left', loc=location, title="Phonon DOS", title_fontproperties={'size':'small'})
    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i, linewidth=0.4, linestyle='-.', c='gray')

    ax1.set_xticks(ticks,labels)
    ax1.set_ylabel('Frequency (THz)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def dosfile(EXPORT, figsize, vertical, horizontal, darr, dele, fill, elements, linestyle, linewidth, legend, location, exchange, color):
    plt.figure(figsize=figsize)
    plt.minorticks_on()
    plt.tick_params(axis='both', which='minor', color='gray')
    num = dele.shape[-1]
    p_dos = []
    if num > len(color):
        color = color + [''] * (num - len(color))

    if num > len(linestyle):
        linestyle = linestyle + ['-'] * (num - len(linestyle))

    if num > len(linewidth):
        linewidth = linewidth + [0.8] * (num - len(linewidth))

    if exchange:
        for i in range(num):
            if color[i]:
                p_dos = p_dos + plt.plot(darr, dele[:,i], linewidth=linewidth[i], linestyle=linestyle[i], color=color[i])
                if fill:
                    plt.fill_between(darr, dele[:,i], 0, color=color[i], alpha=0.2)
            else:
                p_dos = p_dos + plt.plot(darr, dele[:,i], linewidth=linewidth[i], linestyle=linestyle[i])
                if fill:
                    plt.fill_between(darr, dele[:,i], 0, alpha=0.2)

        plt.xlim(vertical)
        plt.ylim(horizontal)
        plt.xlabel('Frequency (THz)')
        plt.ylabel('Phonon DOS')
        plt.tick_params(axis='y', labelsize='medium', labelcolor='dimgray')
    else:
        for i in range(num):
            if color[i]:
                p_dos = p_dos + plt.plot(dele[:,i], darr, linewidth=linewidth[i], linestyle=linestyle[i], color=color[i])
                if fill:
                    plt.fill_between(dele[:,i], darr, 0, color=color[i], alpha=0.2)
            else:
                p_dos = p_dos + plt.plot(dele[:,i], darr, linewidth=linewidth[i], linestyle=linestyle[i])
                if fill:
                    plt.fill_between(dele[:,i], darr, 0, alpha=0.2)

        plt.ylim(vertical)
        plt.xlim(horizontal)
        plt.ylabel('Frequency (THz)')
        plt.xlabel('Phonon DOS')
        plt.tick_params(axis='x', labelsize='medium', labelcolor='dimgray')

    plt.axvline(linewidth=0.4, linestyle='-.', c='gray')
    plt.axhline(linewidth=0.4, linestyle='-.', c='gray')
    if num > len(elements):
        elements = elements + [''] * (num - len(elements))
    elif num < len(elements):
        if num == 1:
            elements = ['$tdos$']
        else:
            elements = elements[:num]

    plt.legend(p_dos, elements, frameon=False, prop={'size':'medium'}, alignment='left', loc=location, title=legend[0], title_fontproperties={'size':'medium'})
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

