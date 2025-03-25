with DAG():
    empty_output_xml = SourceTask(
        task_id = "empty_output_xml", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = XMLFormat(), 
        filePath = {
          "type": "concat_operation", 
          "properties": {
            "elements": [{"type" : "literal", "properties" : {"value" : "error in the data that you throw"}}]
          }
        }
    )
    SFTPSource_1 = SourceTask(
        task_id = "SFTPSource_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "@id"},                         {"dataType" : {"type" : "utf8"}, "name" : "Email"},                         {"dataType" : {"type" : "bool"}, "name" : "IsActive"},                         {"dataType" : {"type" : "utf8"}, "name" : "Name"},                         {"dataType" : {"type" : "int64"}, "name" : "Age"}], 
            "providerType": "arrow"
          }
        ), 
        filePath = "/prophecy-sftp/aruns/records_table.xml"
    )
