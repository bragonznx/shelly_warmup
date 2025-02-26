
**Abstract :**
the purpose of the 2 script is to get a very small rest api running in cerbot GX
The rest API will expose your battery Level and the Power you are producing
function of values you'll launch your water boiler connect to the shelly, or not.
Purpose is to build a pure software solar router



**Changelog :**

✅ "Warm-up" Mode – Relay turns on only if SoC ≥ 85% and Solar ≥ 1000W.

✅ Live Monitoring in Warm-up – If SoC drops below 70% or solar below 1000W, warm-up stops immediately.

✅ Normal Heating Logic – If warm-up succeeds, the script follows normal relay rules.

✅ Fallback Heating at 8:00 PM – If no heating happened, the script runs fallback for 1 hour.

✅ Logging for Debugging – You'll see status updates in the logs.




**Setup :**

1 - put your Cerbot GX in super user

2 - activate SSH

3 - write your script in /data

4 - daemonize it and launch it with daemontool supervisor already include in venus os

5 - install the shelly script in your shelly

6 - customize the values

7 - you are ready to enjoy
