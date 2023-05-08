TITLE = "Welcome to the extractor. That's the tool used for extracting the actual pc process list."
COMMAND_EXAMPLE = "Please execute the coda using: $ python .\\functions\\extractor.py <filename> --args"
HELPER = {
    "--filter-user=<username>": 'Get all the process started and owned by a certain user. '
                                'It will use the param username',
    "--filter-status=<status>": 'Get all the process in a determined status. Status can be "running", "sleeping", '
                                '"stopped" or "zombie". It will be used the "status" key of the process obj.',
    "--filter-cpu=<max_usage>": 'Get all the processes with more than a certain usage of cpu; '
                                'It will use the param cpu_percent',
    "--filter-memory=<max_usage>": 'Get all the processes with more than a certain amount of memory usage; '
                                   'It will use the param proc.info[mem_info].rss. Remember that it include only the '
                                   'physical memory and not the one in the swap mem or the virtual one. Is the real RAM '
                                   'usage indicator',
    "--filter-vmem=<max_usage>": 'Get all the processes with more than a certain amount of virtual mem usage; '
                                 'It will use the param proc.info[mem_info].vms. Remember that it include also the '
                                 'physical mem, the swap mem and the file mapping',
}
