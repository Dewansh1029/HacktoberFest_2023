def get_mem_stats(self, testscript, hdl, feature ):

        log.info( "This proc retuns value of ")
        grand_match=''
        mem_stats_dict={}
        cfg = '''
            show system internal {0} mem-stats detail | last 5
            '''.format(feature)
        try:
            output = hdl.execute(cfg)
        except:
            log.error('Invalid CLI given: %s' % (cfg))
            log.error('Error with cli')
            log.error(sys.exc_info())
            self.failed()
        log.info(output)
        log.info(type(output))
        for k, v in output.items():

            if re.search('Total bytes',v):
                break
            else :
                continue
        grand_match=''
        
        grand_match=re.search('Total bytes:\s+\d+\s+\((\d+)k\)',v)
        log.info(grand_match)
        return(grand_match.group(0))
