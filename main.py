# python3

def process():
  # in a nutshell, kods darbojas tā kā tetris
  threads = [0] * n_threads
  output = []
  for job_duration in jobs:
    # atrod piemērotāko threadu (ar vismazāko apstrādes ilgumu)
    thread_i = threads.index(min(threads))
    # saglabājam, kad darbs tiks sākts
    output.append((thread_i, threads[thread_i]))
    # pieskaita threadam darba ilgumu
    threads[thread_i] += job_duration

  assert n_jobs == len(output)

  print("\n".join([f"{thread_num}, {starts_at}" for thread_num, starts_at in output]))

n_threads = 4
jobs = [2,3,10,2,1,15,100,10,25,32,1,55,23,124,10,2,3,650,3]
n_jobs = len(jobs)

process()



