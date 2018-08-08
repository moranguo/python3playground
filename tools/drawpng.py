import numpy as np
import matplotlib.pyplot as plt


def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height),
                ha='center', va='bottom')


def draw_events(events, figname, title="default title"):
    N = len(events)
    if N <= 0:
        print("no device and events found")
        return
    list_devices = []
    list_events_count = []
    for key in sorted(events):
        list_devices.append(key)
        list_events_count.append(events[key])

    ind = np.arange(N)
    width = 1

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, list_events_count, width, color='b')
    ax.set_ylabel('Events Count')
    if title: title_name = title
    if title:
        ax.set_title(title)
    else:
        ax.set_title("default title")
    ax.set_xticks(ind + width / 2.)
    ax.set_xticklabels(list_devices, rotation='vertical', fontsize='x-small')

    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
    # plt.show()
    plt.savefig(figname, facecolor='w', edgecolor='w', bbox_inches='tight')


def draw_test():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    menStd = (2, 3, 4, 1, 2)

    ind = np.arange(N)  # the x locations for the groups, array([0, 1, 2, 3, 4])
    width = 0.35  # the width of the bars
    # ind + width is array([ 0.35,  1.35,  2.35,  3.35,  4.35])

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

    womenMeans = (25, 32, 34, 20, 25)
    womenStd = (3, 5, 2, 3, 3)
    rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

    # add some
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

    ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.show()


if __name__ == "__main__":
    # draw_test()
    events = {'StarC-ZenossMonitor': 3, 'StarC-E2Email': 4}
    events = {u'StarC-ReInMTA2': 18, u'StarC-InPreMTA3': 20, u'StarC-InPreMTA2': 25, u'StarC-InPreMTA1': 67,
              u'StarC-InPreMTA7': 22, u'StarC-InPreMTA6': 25, u'StarC-InPreMTA5': 21, u'StarC-InPreMTA4': 21,
              u'StarC-InPostMTA6': 15, u'StarC-InPreMTA9': 21, u'StarC-InPreMTA8': 25, u'StarC-InPostMTA3': 16,
              u'StarC-InPostMTA5': 15, u'StarC-InPostMTA1': 21, u'StarC-InPostMTA4': 16, u'StarC-InPostMTA2': 15,
              u'StarC-OutMTA5': 9, u'StarC-OutMTA4': 11, u'StarC-OutMTA7': 9, u'StarC-OutMTA6': 9, u'StarC-OutMTA1': 10,
              u'StarC-OutMTA3': 11, u'StarC-InPreMTA10': 36, u'StarC-OutMTA8': 9, u'StarC-InInMTA6': 19,
              u'StarC-InInMTA4': 17, u'StarC-InInMTA5': 18, u'StarC-InInMTA2': 18, u'StarC-InInMTA3': 17,
              u'StarC-InInMTA1': 25, u'StarC-OutMTA2': 11, u'StarC-ReInMTA1': 16}
    draw_events(events, "test1.png", title="Events Count on Each Device -- MTA\ntime1-time2")
    events_other = {u'StarC-Log4': 16, u'StarC-Log5': 13, u'StarC-Cuplog': 24, u'StarC-JobServer': 2, u'StarC-Log1': 16,
                    u'StarC-Log2': 14, u'StarC-Log3': 17, u'StarC-InFallback1': 23, u'StarC-QTUtilitySlave': 77,
                    u'StarC-QTUtility': 111, u'StarC-QT1': 9, u'StarC-QT2': 9, u'StarC-QT3': 10, u'StarC-Register': 77,
                    u'StarC-Au': 17, u'E2E-MailMonitor': 118, u'StarC-Bridge-Master': 2, u'StarC-Policy': 17}
    draw_events(events_other, "test2.png", title="Events Count on Each Device -- Non MTA")
