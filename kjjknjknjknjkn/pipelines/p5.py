with DAG():
    prophecy__temp_p5_post_SFTPSource_1_0 = Task(
        task_id = "prophecy__temp_p5_post_SFTPSource_1_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_p5_post_SFTPSource_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_p5_source", 
          "alias": ""
        }
    )
    user_information_csv = Task(
        task_id = "user_information_csv", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/test_results.csv"}}]
            }
          }
        }, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    user_information_csv_1_1 = Task(
        task_id = "user_information_csv_1_1", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {"category" : "file", "kind" : "json", "properties" : {}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/test_results.json"}}]
            }
          }
        }
    )
    SFTPSource_1 = SourceTask(
        task_id = "SFTPSource_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(
          header = True, 
          schema = {
            "fields": [{"dataType" : {"type" : "int64"}, "name" : "id"},                         {"dataType" : {"type" : "utf8"}, "name" : "name"},                         {"dataType" : {"type" : "utf8"}, "name" : "email"},                         {"dataType" : {"type" : "int64"}, "name" : "age"},                         {"dataType" : {"type" : "utf8"}, "name" : "city"},                         {"dataType" : {"type" : "utf8"}, "name" : "country"}], 
            "providerType": "arrow"
          }, 
          separator = ","
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records.csv"
    )
    model_p5_Limit_1 = Task(task_id = "model_p5_Limit_1", component = "Model", modelName = "model_p5_Limit_1")
    model_p5_OrderBy_1 = Task(task_id = "model_p5_OrderBy_1", component = "Model", modelName = "model_p5_OrderBy_1")
    user_information_csv_1 = Task(
        task_id = "user_information_csv_1", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {"category" : "file", "kind" : "json", "properties" : {}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/test_results.json"}}]
            }
          }
        }
    )
    (
        prophecy__temp_p5_post_SFTPSource_1_0.output_port_0_1
        >> [user_information_csv_1_1.in0, model_p5_OrderBy_1.in_1, model_p5_Limit_1.in_1]
    )
    SFTPSource_1.out0 >> prophecy__temp_p5_post_SFTPSource_1_0.input_port_0_1
    model_p5_Limit_1.out_1 >> user_information_csv_1.in0
    model_p5_OrderBy_1.out_1 >> user_information_csv.in0
