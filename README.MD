**GET /profile**
The server application allows a user to create only one user profile. The get request handler only evers return a singular JSON object. 

**POST /profile**

Your server should allow for an incoming POST request that accepts a JSON body.

The `last_updated` attribute should be generated by the web application and can be formatted any way you choose (it MUST include both date and time), as long as it reflects the time at the time of the request. The `last_updated` attribute should not be sent to the web application by the client.

(Here’s that really good idea I had) The profile’s `last_updated` attribute’s value should update every time the web application successfully handles a tank POST, PUT and DELETE request. The value should reflect the date and time that any of those three requests is successful 

**GET /tank**

This route should return a **list** of 0 or more objects. 

If a POST request was successfully made to the /tank route previously, the GET route should return a **list** of the previously POSTed tank objects. 


**GET /tank/{id}**

This route should return a **single JSON object** of a tank that is associated with the id passed as input in the route. If the API is unable to locate the tank object that has the id specified, the API should respond with **an appropriate response message and status code that reflects this**. 


**POST /tank**

This route should accepts a JSON object structured as depicted in *[fig.5](https://www.notion.so/lab-959a3128adfb4ed99fcb5868d90a0f94?pvs=21).* On success, the web application should respond with the the same JSON object that was POSTed with the addition of an `id` attribute. This `id` is to be generated by the database. 


**PATCH /tank/{id}**

Your server should allow a client to alter the parts of one of the tanks after it has been POSTed. The web application should allow the client to send a request with a JSON body that has any combination of the three attributes and update them as necessary (The client should **NOT** be allowed to edit the `id` attribute). 

The route should also return status code that indicates that an object was **successfully altered**. 



**DELETE /tank/{id}**

Your web application should allow the client to delete any previously POSTed object. The web application should not send back any message to the client once the objects has been deleted. There should, however, be a suitable status code that indicates **success** and that an **empty response is expected**. 



Purpose of Code: We all know by this point how this goes 


Would you rather go on a double date with your ex or clog the toilet on a first date?? (I would personally not do either)
