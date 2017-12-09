package HALA.CIS450;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.ItemCollection;
import com.amazonaws.services.dynamodbv2.document.QueryOutcome;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.spec.QuerySpec;
import com.amazonaws.services.dynamodbv2.document.utils.ValueMap;
import com.amazonaws.services.dynamodbv2.model.AttributeValue;
import com.amazonaws.services.dynamodbv2.model.ScanRequest;
import com.amazonaws.services.dynamodbv2.model.ScanResult;

/**
 * Hello world!
 *
 */
public class App 
{
	static Table cupidtable;
	static Table zillowtable;
	static AmazonDynamoDB client;
    public static void main( String[] args )
    {
    	initiate();
    	genderorientation();
    }
    public static void initiate(){
    	client = AmazonDynamoDBClientBuilder.standard()
    			.withRegion(Regions.US_EAST_1).build();
    			DynamoDB dynamoDB = new DynamoDB(client);
    			cupidtable = dynamoDB.getTable("okcupidsmall");
    			//cupidtable = dynamoDB.getTable("OkCupid");
    			zillowtable = dynamoDB.getTable("Zillow");
    }
    
    public static String genderorientation(){
    	StringBuilder sb = new StringBuilder();
    	sb.append("count,descriptor\n");
		Map<String, AttributeValue> expressionAttributeValues = new HashMap<String, AttributeValue>();
		expressionAttributeValues.put(":valerie", new AttributeValue().withS("f")); 
		expressionAttributeValues.put(":orientation", new AttributeValue().withS("straight")); 
		ScanRequest scanRequest = new ScanRequest()
		   // .withTableName("OkCupid")
			.withTableName("okcupidsmall")
		    .withFilterExpression("sex = :valerie and orientation = :orientation")
		    .withExpressionAttributeValues(expressionAttributeValues);
		
		ScanResult result = client.scan(scanRequest);
		sb.append(result.getCount().toString() + ","+"straight females\n");
		
		ScanRequest scanRequest2 = new ScanRequest()
				   // .withTableName("OkCupid")
					.withTableName("okcupidsmall")
				    .withFilterExpression("sex = :valerie and orientation <> :orientation")
				    .withExpressionAttributeValues(expressionAttributeValues);
				
		ScanResult result2 = client.scan(scanRequest2);
		sb.append(result2.getCount().toString() + ","+"gay females\n");
		
		ScanRequest scanRequest3 = new ScanRequest()
				   // .withTableName("OkCupid")
			.withTableName("okcupidsmall")
			.withFilterExpression("sex = :valerie and orientation = :orientation")
		    .withExpressionAttributeValues(expressionAttributeValues);
				
			ScanResult result3 = client.scan(scanRequest3);
			sb.append(result3.getCount().toString() + ","+"straight males\n");
				
		ScanRequest scanRequest4 = new ScanRequest()
						   // .withTableName("OkCupid")
			.withTableName("okcupidsmall")
			.withFilterExpression("sex = :valerie and orientation <> :orientation")
			.withExpressionAttributeValues(expressionAttributeValues);
						
		ScanResult result4 = client.scan(scanRequest4);
		sb.append(result4.getCount().toString() + ","+"gay males");
		
		System.out.println(sb.toString());
		return sb.toString();
    }
    
    public static String ageorientation(){
    	StringBuilder sb = new StringBuilder();
    	sb.append("count,descriptor\n");
		Map<String, AttributeValue> expressionAttributeValues = new HashMap<String, AttributeValue>();
		expressionAttributeValues.put(":val", new AttributeValue().withS("f")); 
		expressionAttributeValues.put(":orientation", new AttributeValue().withS("straight")); 
		ScanRequest scanRequest = new ScanRequest()
		   // .withTableName("OkCupid")
			.withTableName("okcupidsmall")
		    .withFilterExpression("sex = :val and orientation = :orientation")
		    .withExpressionAttributeValues(expressionAttributeValues);
		
		ScanResult result = client.scan(scanRequest);
		sb.append(result.getCount().toString() + ","+"straight females\n");
		
		ScanRequest scanRequest2 = new ScanRequest()
				   // .withTableName("OkCupid")
					.withTableName("okcupidsmall")
				    .withFilterExpression("sex = :valerie and orientation <> :orientation")
				    .withExpressionAttributeValues(expressionAttributeValues);
				
		ScanResult result2 = client.scan(scanRequest2);
		sb.append(result2.getCount().toString() + ","+"gay females\n");
		
		ScanRequest scanRequest3 = new ScanRequest()
				   // .withTableName("OkCupid")
			.withTableName("okcupidsmall")
			.withFilterExpression("sex = :valerie and orientation = :orientation")
		    .withExpressionAttributeValues(expressionAttributeValues);
				
			ScanResult result3 = client.scan(scanRequest3);
			sb.append(result3.getCount().toString() + ","+"straight males\n");
				
		ScanRequest scanRequest4 = new ScanRequest()
						   // .withTableName("OkCupid")
			.withTableName("okcupidsmall")
			.withFilterExpression("sex = :valerie and orientation <> :orientation")
			.withExpressionAttributeValues(expressionAttributeValues);
						
		ScanResult result4 = client.scan(scanRequest4);
		sb.append(result4.getCount().toString() + ","+"gay males");
		
		System.out.println(sb.toString());
		return sb.toString();
    }
    
}
