class Solution(object):
    def reformatDate(self, date):
        x,y,z=date.split( )
        if len(x)==3:
            day='0'+x[0]
        else:
            day=x[:2] 
        month={
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12',
        } 
           
        return z +"-"+month[y]+"-"+day     
        
        
        
