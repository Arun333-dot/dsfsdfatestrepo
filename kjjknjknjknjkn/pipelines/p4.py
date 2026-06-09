with DAG():
    model_p4_Reformat_1_2 = Task(
        task_id = "model_p4_Reformat_1_2", 
        component = "Model", 
        modelName = "model_p4_Reformat_1_2"
    )
    model_p4_OrderBy_1_1 = Task(
        task_id = "model_p4_OrderBy_1_1", 
        component = "Model", 
        modelName = "model_p4_OrderBy_1_1"
    )
    SFTPSource_1 = SourceTask(
        task_id = "SFTPSource_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(
          header = True, 
          separator = ",", 
          schema = {
            "fields": [{"name" : "id", "dataType" : {"type" : "int64"}},                         {"name" : "name", "dataType" : {"type" : "utf8"}},                         {"name" : "email", "dataType" : {"type" : "utf8"}},                         {"name" : "age", "dataType" : {"type" : "int64"}},                         {"name" : "city", "dataType" : {"type" : "utf8"}},                         {"name" : "country", "dataType" : {"type" : "utf8"}}], 
            "providerType": "arrow"
          }
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records.csv"
    )
    user_information_json = Task(
        task_id = "user_information_json", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/test_results.json"}}]
            }
          }
        }, 
        format = {"properties" : {}, "kind" : "json", "category" : "file"}
    )
    user_information_xml = Task(
        task_id = "user_information_xml", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/test_results.xml"}}]
            }
          }
        }, 
        format = {"properties" : {"rootName" : "root", "rowTag" : "row"}, "kind" : "xml", "category" : "file"}
    )
    user_information_csv_1 = Task(
        task_id = "user_information_csv_1", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/test_results.xlsx"}}]
            }
          }
        }, 
        format = {
          "properties": {"sheetName" : "Sheet1", "header" : True, "ignoreCellFormatting" : True}, 
          "kind": "xlsx", 
          "category": "file"
        }
    )
    model_p4_OrderBy_1_1_2 = Task(
        task_id = "model_p4_OrderBy_1_1_2", 
        component = "Model", 
        modelName = "model_p4_OrderBy_1_1_2"
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
    prophecy__temp_p4_post_SFTPSource_1_0 = Task(
        task_id = "prophecy__temp_p4_post_SFTPSource_1_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_p4_post_SFTPSource_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_p4_source", 
          "alias": ""
        }
    )
    model_p4_OrderBy_1_1_1 = Task(
        task_id = "model_p4_OrderBy_1_1_1", 
        component = "Model", 
        modelName = "model_p4_OrderBy_1_1_1"
    )
    model_p4_OrderBy_1_1_2.out_1 >> user_information_xml.in0
    model_p4_OrderBy_1_1_1.out_1 >> user_information_json.in0
    (
        prophecy__temp_p4_post_SFTPSource_1_0.output_port_0_1
        >> [model_p4_OrderBy_1_1_1.in_1, model_p4_OrderBy_1_1_2.in_1, model_p4_OrderBy_1_1.in_1,
              model_p4_Reformat_1_2.in_1]
    )
    SFTPSource_1.out0 >> prophecy__temp_p4_post_SFTPSource_1_0.input_port_0_1
    model_p4_OrderBy_1_1.out_1 >> user_information_csv_1.in0
    model_p4_Reformat_1_2.out_1 >> user_information_csv.in0
