## EMQX Broker Configuration

I am using a self-hosted EMQX broker deployed on Railway.

Two separate users have been configured:
- One user for the Wokwi ESP32 client
- One user for the Node-RED backend

Anonymous access is disabled and only authenticated users are allowed to connect.

### user 1
username: esp32

password **********

allowed subscribe to:
lnu/iot/{STUDENT_ID}/command/led

allowed publish to:
lnu/iot/{STUDENT_ID}/sensor

### user 2:
username node-red

password **********

allowed subscribe to:
lnu/iot/{STUDENT_ID}/sensor

allowed publish to:
lnu/iot/{STUDENT_ID}/command/led

### Risk comparison between public broker and self-hosted broker

| Public Broker | Self-hosted Broker |
|---|---|
| Shared with other users | Fully controlled environment |
| Lower security | Authentication and ACL enabled |
| No topic isolation | Restricted publish/subscribe permissions |
| Public access | Controlled user access |

Even though the self-hosted broker has better controll and authentication, there is always a security risk with passwords and an attacker getting access to my users or in worst case scenerio, they get access to the admin dashboard.

I have changed the admin password to one much more secure to make sure nobody gets access to these things.

### below is a few pictures showing some of the security decisions:

<img width="2440" height="529" alt="image" src="https://github.com/user-attachments/assets/b9b0938a-e333-40ca-9147-a82cffdb0ce1" />
