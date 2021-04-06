## A

1. Create the pod using:
````kubectl apply -f deploymentA.yml ````
2. Get the pod using 
````kubectl get pods hello ````
This produces the following output:
````NAME    READY   STATUS    RESTARTS   AGE
hello   1/1     Running   0          10s ````

3. Check the logs using 
````kubectl logs hello ````
Which produces the following output:
````Hello, ````
This is expected because the computer running the pod will not have that environment variable

4. Delete the pod using
````kubectl delete pods hello ````

## B

1. Create the pod using:
````kubectl apply -f deploymentB.yml ````
2. Check the logs using
````kubectl logs hello ````
Which produces the following output:
````Hello,  Sierra ````
3. Delete the pod using
````kubectl delete pods hello ````

## C

1. Create the deployment using:
````kubectl apply -f deploymentC.yml ````
2. Get all pods with their IP addresses using
````kubectl get pods -o wide ````
Which produces the following output:
````NAME                                    READY   STATUS    RESTARTS   AGE     IP             NODE     NOMINATED NODE   READINESS GATES
hello-6b9c4c9764-bsk9p                  1/1     Running   0          7m4s    10.244.3.35    c01      <none>           <none>
hello-6b9c4c9764-dzdjn                  1/1     Running   0          7m4s    10.244.6.127   c03      <none>           <none>
hello-6b9c4c9764-gqszt                  1/1     Running   0          7m4s    10.244.5.89    c04      <none>           <none> ````
3. Check the logs using
````kubectl logs hello-6b9c4c9764-bsk9p ````
Which produces the following output:
````Hello,  Sierra  from IP  10.244.3.35 ````
````kubectl logs hello-6b9c4c9764-dzdjn ````
Which produces the following output:
````Hello,  Sierra  from IP  10.244.6.127 ````
````kubectl logs hello-6b9c4c9764-gqszt ````
Which produces the following output:
````Hello,  Sierra  from IP  10.244.5.89 ````

These results do match the IP address found in 2.
