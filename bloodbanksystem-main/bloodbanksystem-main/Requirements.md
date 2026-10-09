\# Blood Bank Inventory \& Emergency Donor Matcher



\## Functional Requirements



| ID | Type | Description | Priority | Acceptance Criteria | Rationale |

| --- | --- | --- | --- | --- | --- |

| FR-001 | Functional | The system shall record and track blood component inventory including blood group, component type, quantity, and expiry date. | High | Inventory details can be added, updated, and viewed correctly. | Enables accurate monitoring of available blood stock. |

| FR-002 | Functional | The system shall validate emergency blood requests and identify the required blood group and component. | High | Valid emergency requests are accepted and incomplete requests are rejected. | Ensures that emergency requests contain the information needed for matching. |

| FR-003 | Functional | The system shall cross-reference emergency blood requests with available compatible blood inventory. | High | The system correctly identifies compatible available units. | Helps determine whether the blood bank can satisfy an emergency request. |

| FR-004 | Functional | The system shall identify eligible compatible donors within a 10 km radius during critical shortages. | High | Compatible eligible donors within 10 km are identified. | Enables targeted emergency donor matching. |

| FR-005 | Functional | The system shall send emergency notifications to compatible eligible donors during critical shortages. | High | Matching donors receive notifications within 30 seconds. | Helps obtain blood quickly when inventory is insufficient. |



\## Non-Functional Requirements



| ID | Type | Description | Priority | Acceptance Criteria | Rationale |

| --- | --- | --- | --- | --- | --- |

| NFR-001 | Performance \& Security | The inventory ledger shall maintain transactional consistency and prevent simultaneous allocation of the same blood unit. | High | Testing confirms that the same blood unit cannot be allocated to multiple requests simultaneously. | Prevents incorrect inventory allocation and maintains data integrity. |

| NFR-002 | Performance | Emergency donor matching and notification shall be completed within 30 seconds under normal operating conditions. | High | Performance testing confirms donor notifications are generated within 30 seconds. | Emergency situations require rapid donor notification. |

