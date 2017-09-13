import json
import unit_ids

js_path = raw_input('Drag json data here:').strip('"')

dudes = json.loads(open(js_path).read())['unit_list']
time_list = [(x['create_time'],x['class'],x['unit_master_id'],x['unit_level']) for x in dudes]
time_list.sort()

output = open('\\'.join(js_path.split('\\')[:-1]) + '\\results.csv','w')
output.write(','.join(['Date Summoned','Current *','Name','Level\n']))
for x in time_list:
	try:
		output.write(','.join([x[0],str(x[1]),unit_ids.monsters_name_map[str(x[2])],str(x[3])]) + '\n')
	except:
		if len(str(x[2])) == 7:
			output.write(','.join([x[0],str(x[1]),'Homunculus',str(x[3])]) + '\n')
			continue
		if unit_ids.monsters_name_map[str(x[2]+10)] == '':
			unit_name = unit_ids.monsters_name_map[str(x[2])[:3]]
		else:
			unit_name = unit_ids.monsters_name_map[str(x[2]+10)] + ' (Unawakened)'
		output.write(','.join([x[0],str(x[1]),unit_name,str(x[3])]) + '\n')
		

output.close()
print('Results located at :' + '\\'.join(js_path.split('\\')[:-1]) + '\\results.csv')