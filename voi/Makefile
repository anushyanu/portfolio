all: clean generate_spec generate_db

generate_spec:
	cd scripts && ./convert_spec_to_python.py
	# if generic
	# cd scripts && ./convert_spec_to_python.py -i old_req/anushya/yanu/voi_spec.txt -o scripts/voi_spec.py

generate_db:
	cd db && python db_app.py
	cp db/customer.db .

clean:
	rm -f scripts/voi_spec.py
	rm -rf db/__py* __py*
	rm -f *.db db/*.db

