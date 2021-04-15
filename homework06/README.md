# Homework 06

Included in this directory is all yml files for the applicable testing deployments and services, as well as a yml for the python debug environment deployment and the files necessary for push the previously made Flask app to Docker Hub.

## Usage

Use the following commands to start the deployments and services.

Step 1:

````kubectl apply -f sierrao-test-pvc.yml````

Step 2:

````kubectl apply -f sierrao-test-redis-deployment.yml````

Step 3:

````kubectl apply -f sierrao-test-redis-service.yml````

Find the IP address of the test redis service by running 

````kubectl get services -o wide ````

If the python debug container is not already running, deploy it using:

````kubectl -f apply deployment-python-debug.yml````

Find the pod name using:

````kubectl get pods````

And exec into the container using:

````kubectl exec -it <pod_name> -- /bin/bash````

Once inside, run 
````pip install redis ```` and then launch the python shell with ````ipython````. Inside the python shell, run ````import redis```` then create a redis client object using ```` rd = redis.StrictRedis(host='10.96.134.73', port=6379, db=0) ```` where host is the IP adress of the redis service previously found. Now run ````rd.set('my_key', 'my_value') ```` followed by ````rd.get('my_key')```` and ensure the output is b'my_value'. 

Now in another shell run ````kubectl delete <redis pod name> ```` using the name previously found to delete the pod. 

Now return to the original terminal in the python shell and run ````rd.get('my_key')```` again and ensure the output is still b'my_value'. 

Step 4:

````kubectl apply -f sierrao-test-flask-deployment.yml````

Step 5:

````kubectl apply -f sierrao-test-flask-service.yml````

To ensure everything is up and running, use:

````kubectl get pods --selector username=sierrao````

````kubectl get deployments --selector username=sierrao````

````kubectl get services````


````kubectl get pvc --selector username=sierrao````


Now you should be able to curl the flask app at the specified IP at port 5000 using the endpoints from the midterm assignment.