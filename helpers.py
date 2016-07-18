import csv
import math

def write_log(timestamp, task, data, in_rows, out_rows, solution, fun, run, time_sec, mem_gb):
   csv_file = os.environ['CSV_TIME_FILE']
   if math.isnan(time_sec):
      time_sec = ""
   if math.isnan(mem_gb):
      mem_gb = ""
   log_row = [timestamp, task, data, in_rows, out_rows, solution, fun, run, time_sec, mem_gb]
   log_header = ["timestamp","task","data","in_rows","out_rows","solution","fun","run","time_sec","mem_gb"]
   append = os.path.isfile(csv_file)
   print('# ' + ','.join(str(x) for x in log_row))
   if append:
      with open(csv_file, 'a') as f:
         w = csv.writer(f)
         w.writerow(log_row)
   else:
      with open(csv_file, 'w+') as f:
         w = csv.writer(f)
         w.writerow(log_header)
         w.writerow(log_row)
   return True