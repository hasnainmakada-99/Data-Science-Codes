import numpy as np

# Local dataset stored using predefined dictionaries
shipment_data = {
    "Warehouse 1": [120, 135, 128, 142, 150, 160, 155],
    "Warehouse 2": [98, 105, 110, 115, 120, 118, 125],
    "Warehouse 3": [140, 145, 150, 155, 165, 170, 175],
    "Warehouse 4": [80, 85, 90, 95, 100, 105, 110]
}

transport_cost_data = {
    "Warehouse 1": [12, 12, 13, 13, 14, 14, 15],
    "Warehouse 2": [10, 11, 11, 12, 12, 13, 13],
    "Warehouse 3": [14, 14, 15, 15, 16, 16, 17],
    "Warehouse 4": [9, 9, 10, 10, 11, 11, 12]
}

capacity_data = {
    "Warehouse 1": 175,
    "Warehouse 2": 145,
    "Warehouse 3": 180,
    "Warehouse 4": 120
}

warehouses = np.array(list(shipment_data.keys()))
weeks = np.array(["Week 1", "Week 2", "Week 3", "Week 4",
                "Week 5", "Week 6", "Week 7"])
shipments = np.array(list(shipment_data.values()))
transport_cost = np.array(list(transport_cost_data.values()))
capacity = np.array(list(capacity_data.values()))

print("WAREHOUSE SHIPMENT MATRIX")
print(shipments)
print("Shape:", shipments.shape)

print("\nTRANSPORTATION COST MATRIX")
print(transport_cost)
print("Shape:", transport_cost.shape)

average_shipments = np.mean(shipments)
shipment_std = np.std(shipments)

print("\nAVERAGE AND STANDARD DEVIATION")
print("Average shipments:", round(average_shipments, 2))
print("Standard deviation:", round(shipment_std, 2))

sliced_shipments = shipments[:2, -3:]
print("\nFIRST TWO WAREHOUSES AND LAST THREE WEEKS")
print(sliced_shipments)
print("Sliced shape:", sliced_shipments.shape)

reshaped_shipments = shipments.reshape(7, 4)
print("\nRESHAPED SHIPMENT MATRIX")
print(reshaped_shipments)
print("Reshaped shape:", reshaped_shipments.shape)

transportation_expense = np.multiply(shipments, transport_cost)
print("\nELEMENT-WISE TRANSPORTATION EXPENSE")
print(transportation_expense)

warehouse_totals = np.sum(shipments, axis=1)
weekly_totals = np.sum(shipments, axis=0)
warehouse_costs = np.sum(transportation_expense, axis=1)
average_unit_cost = warehouse_costs / warehouse_totals
utilization = shipments / capacity[:, None] * 100
maximum_utilization = np.max(utilization, axis=1)

best_warehouse_index = np.argmax(warehouse_totals)
peak_week_index = np.argmax(weekly_totals)
efficient_warehouse_index = np.argmin(average_unit_cost)
bottleneck_index = np.argmax(maximum_utilization)
bottleneck_points = np.where(utilization >= 90)

print("\nWAREHOUSE PERFORMANCE REPORT")
for i in range(len(warehouses)):
    print(warehouses[i])
    print("  Total shipments:", warehouse_totals[i])
    print("  Average weekly shipments:", round(np.mean(shipments[i]), 2))
    print("  Transportation expense:", warehouse_costs[i])
    print("  Average cost per shipment:", round(average_unit_cost[i], 2))
    print("  Maximum capacity utilization:",
        round(maximum_utilization[i], 2), "%")

print("\nWEEKLY INVENTORY MOVEMENT")
for i in range(len(weeks)):
    print(weeks[i], ":", weekly_totals[i])

print("\nLOGISTICS BOTTLENECK POINTS")
for warehouse_i, week_i in zip(*bottleneck_points):
    print(warehouses[warehouse_i], weeks[week_i],
        "Utilization:", round(utilization[warehouse_i, week_i], 2), "%")

print("\nSUPPLY CHAIN PLANNING SUMMARY")
print("Highest-performing warehouse:",
    warehouses[best_warehouse_index])
print("Peak shipment week:", weeks[peak_week_index])
print("Most cost-efficient warehouse:",
    warehouses[efficient_warehouse_index])
print("Highest bottleneck risk:", warehouses[bottleneck_index])
print("Total shipments:", np.sum(shipments))
print("Total transportation expense:", np.sum(transportation_expense))
