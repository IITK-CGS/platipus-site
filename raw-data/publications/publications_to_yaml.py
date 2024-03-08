import bib2yaml as bib
import yaml

bib_file = "publications.bib"
bib.bib2yaml(bib_file, "./", "publications") # produces publications.yml

yaml_file = "publications.yml"
with open(yaml_file) as _in:
	allpubs = yaml.safe_load(_in)

# hugo publications data dir relative to this file
data_dir = "../../data/publications/"

# generate "by_year.yaml"
with open(data_dir + "by_year.yml", "w") as out:
	by_year = dict()
	for pub in allpubs:
		year = pub["year"]
		if year not in by_year: by_year[year] = []
		by_year[year].append(pub)
	# print(by_year)
	by_year = [{x: by_year[x]} for x in by_year]
	# print(by_year)
	# print(type(by_year))
	# sorted(by_year, reverse=True)
	yaml.dump(by_year, out, allow_unicode=True)

# generate "by_topic.yaml"
with open(data_dir + "by_topic.yml", "w") as out:
	by_topic = dict()
	for pub in allpubs:
		topics = pub["keywords"].split(",")
		topics = [t.strip() for t in topics if len(t.strip())>0]
		if len(topics) == 0:
			if "Miscellaneous" not in by_topic:
				by_topic["Miscellaneous"] = []
			by_topic["Miscellaneous"].append(pub)
		for topic in topics:
			if topic not in by_topic: by_topic[topic] = []
			by_topic[topic].append(pub)
	# print(by_topic)
	# by_topic = [{x: by_topic[x]} for x in by_topic]
	# print(by_topic)
	# print(type(by_topic))
	# sorted(by_topic, reverse=True)
	yaml.dump(by_topic, out, allow_unicode=True)
