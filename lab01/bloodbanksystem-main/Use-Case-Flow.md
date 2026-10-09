\# Use-Case Flow Specification



\## Use Case: Emergency Blood Request \& Donor Matching



\### Preconditions



1\. The Emergency Requester has access to the system.

2\. The required blood group and blood component are known.

3\. The blood bank inventory is available in the system.

4\. Donor information is available for eligible donor matching.



\### Postconditions



1\. The emergency blood request is recorded.

2\. Available compatible blood units are identified or reserved.

3\. If there is a critical shortage, compatible eligible donors are identified.

4\. Emergency notifications are sent to matching donors.



\### Main Success Scenario



1\. The Emergency Requester submits an emergency blood request.

2\. The system validates the request.

3\. The system identifies the required blood group and component.

4\. The system checks the blood bank inventory.

5\. The system cross-references the request with compatible available blood units.

6\. If sufficient blood is unavailable, the system identifies compatible eligible donors.

7\. The system filters eligible donors within a 10 km radius.

8\. The system sends emergency notifications to the matching donors.

9\. The system records the notification and emergency request status.



\### Alternate Flow



\*\*A1. Compatible Blood Is Available\*\*



1\. The system finds sufficient compatible blood units in inventory.

2\. The system reserves the required units.

3\. The system updates the inventory.

4\. Emergency donor notifications are not sent.

5\. The emergency request is marked as fulfilled.

