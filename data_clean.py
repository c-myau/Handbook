import sys
import stat_data

def main():
	print("100 values for stats")
	for item in stat_data.artifact_type.items():
		stat_txt = "Main Stat: {stat} | Sum of Probabilites: {chance_sum}\n"
		print(stat_txt.format(stat = item[0], chance_sum = item[1]["chnc"].sum()))

		for attr in item[1]["attr"]:
			stat_txt = "Sub Stat: {attr_name} | Sum of Probabilites: {chance_sum}"
			print(stat_txt.format(attr_name = attr, chance_sum = item[1]["chnc"].sum()))
if __name__ == "__main__":
    sys.exit(main())