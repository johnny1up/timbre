import sys
from os.path import expanduser
import pickle

home = expanduser("~")
sys.path.append(home + '/AXAFLIB/timbre/')
from timbre import *

model_specs = load_model_specs()

msid = 'pftank2t'
limit = 100

datestamp = DateTime().caldate[:9]

init = {'pftank2t': f_to_c(95.), 'pf0tank2t': f_to_c(95.), 'eclipse': False}

if __name__ == "__main__":

    state_pairs = [({'t_dwell1': t1, 'pitch': p1, 'roll': 0.0}, {'pitch': p2, 'roll': 0.0})
                   for p1 in range(45, 170, 1)
                   for p2 in range(45, 170, 1)
                   for t1 in [80000, 90000, 100000]]
    date = '2020:001:00:00:00'
    t1 = DateTime().secs
    results = run_state_pairs(msid, model_specs[msid], init, limit, date, None, state_pairs)
    t2 = DateTime().secs
    print('took {} seconds, for {} state pairs'.format(t2 - t1, len(state_pairs)))
    pickle.dump(results, open('pftank2t_{}_{}.pkl'.format(datestamp, 2), 'wb'))

    state_pairs = [({'t_dwell1': t1, 'pitch': p1, 'roll': 0.0}, {'pitch': p2, 'roll': 0.0})
                   for p1 in range(45, 170, 1)
                   for p2 in range(45, 170, 1)
                   for t1 in [10000, 20000]]
    date = '2019:182:00:00:00'
    t1 = DateTime().secs
    results = run_state_pairs(msid, model_specs[msid], init, limit, date, None, state_pairs)
    t2 = DateTime().secs
    print('took {} seconds, for {} state pairs'.format(t2 - t1, len(state_pairs)))
    pickle.dump(results, open('pftank2t_{}_{}.pkl'.format(datestamp, 3), 'wb'))