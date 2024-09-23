import re
from datetime import datetime

def transform_date_format(dates):
    transformed_dates = []
    
    for date in dates:
        try:
            if re.match(r'\d{4}/\d{2}/\d{2}', date):
                formatted_date = datetime.strptime(date, "%Y/%m/%d").strftime("%Y%d%m")
                transformed_dates.append(formatted_date)
            
            elif re.match(r'\d{2}-\d{2}-\d{4}', date):
                formatted_date = datetime.strptime(date, "%m-%d-%Y").strftime("%Y%d%m")
                transformed_dates.append(formatted_date)
            
        
            elif re.match(r'(\d)\s?(\d{3})p\s?(\d{2})p\s?(\d{2})', date):
                match = re.match(r'(\d)\s?(\d{3})p\s?(\d{2})p\s?(\d{2})', date)
                year = match.group(1) + match.group(2)
                day = match.group(3)
                month = match.group(4)
                
                formatted_date = f"{year}{day}{month}"
                transformed_dates.append(formatted_date)
        
        except ValueError:
            continue
    
    return transformed_dates

if __name__ == "__main__":
    dates = transform_date_format([
        "2010/02/20", 
        "2 016p 19p 12", 
        "11-18-2012", 
        "2018 12 24", 
        "20130720"
    ])
    print(*dates, sep='\n')