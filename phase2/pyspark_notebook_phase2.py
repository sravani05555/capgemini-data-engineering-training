from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("practice").getOrCreate()
customers_data = [(1, "Ravi", "Hyderabad", 25), 
                 (2, "sita", "Chennai", 32),
                 (3, "Arun", "Hyderabad", 28),
                 (4, "Meena", "Bengaluru", 35),
                 (5, "Kiran", "Chennai", 22)]
orders_data = [(101, 1, 2500, "2026-03-01"),
               (102, 2, 1800, "2026-03-02"),
               (103, 1, 3200, "2026-03-03"),
               (104, 3, 1500, "2026-03-04"),
               (105, 5, 2800, "2026-03-05")]
customers = spark.createDataFrame(customers_data, ["customer_id", "customer_name", "city", "age"])
orders = spark.createDataFrame(orders_data, ["order_id", "customer_id", "amount", "order_date"])
--1
orders.groupBy("customer_id").sum("amount").show()
--2
orders.groupBy("customer_id").sum("amount").orderBy("sum(amount)", ascending=False).show(3)
--3
customers.join(orders, "customer_id", "left_anti").show()
--4
customers.join(orders, "customer_id").groupBy("city").sum("amount").show()
--5
orders.groupBy("customer_id").avg("amount").show()
--6
orders.groupBy("customer_id").count().filter("count > 1").show()
--7
orders.groupBy("customer_id").sum("amount").orderBy("sum(amount)", ascending=False).show()
