from multiprocessing import Process

class Pool(object):
    def __init__(self, max_num_of_processes, func, params_list):
        self.max_num_of_processes = max_num_of_processes
        self.func = func
        self.params_list = params_list
        self.processes = []
        self.active_processes = []

    def run(self):
        for par in self.params_list:
            # print "process params: "
            # print par
            p = Process(target=self.func, args=par)
            self.processes.append(p)

        if len(self.params_list) < self.max_num_of_processes:
            self.max_num_of_processes = len(self.params_list)

        while self.processes != []:
            # Remove inactive processes
            for idx, p in enumerate(self.active_processes):
                if not p.is_alive():
                    #print "join!"
                    del self.active_processes[idx]

            remaining_slots = self.max_num_of_processes - len(self.active_processes)
            for i in range(remaining_slots):
                # no more pending processes
                if len(self.processes) == 0:
                    break

                # get a pending process to one of the remaining spots
                p = self.processes.pop(0)
                p.start()
                #print "spawn!"
                #print "active processes: %d" % len(self.active_processes)
                self.active_processes.append(p)

        [p.join() for p in self.active_processes]
