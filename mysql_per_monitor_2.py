    package com.bisal.zb;

    import java.io.FileNotFoundException;
    import java.io.FileReader;
    import java.io.FileWriter;
    import java.io.IOException;

    import com.google.gson.JsonArray;
    import com.google.gson.JsonIOException;
    import com.google.gson.JsonObject;
    import com.google.gson.JsonParser;
    import com.google.gson.JsonSyntaxException;

    public class ZB_1 {
        public static void main(String[] args) {
            try {
                JsonParser parser = new JsonParser(); // 创建JSON解析器
                JsonObject object = (JsonObject) parser.parse(new FileReader(
                        "file/zhiban.log")); // 创建JsonObject对象
                JsonArray array = object.get("dlist").getAsJsonArray();

                // 得到为json的数组
                FileWriter writer = new FileWriter("file/output1.txt");
                String dName;
                String dPerson;
                String dEmail;
                String dPhone;
                String dDate;
                for (int i = 0; i < array.size(); i++) {
                    JsonObject subObject = array.get(i).getAsJsonObject();
                    dutyName = subObject.get("dName").getAsString();
                    dutyPerson = subObject.get("dPerson").getAsString();
                    dutyPhone = subObject.get("dPhone").getAsString();
                    dutyEmail = subObject.get("dEmail").getAsString();
                    dutyDate = subObject.get("startDate").getAsString()
                            .substring(0, 10);
                    writer.write("日期=[" + dDate + "] 值班项=[" + dName
                            + "] 值班人=[" + dPerson + "] 邮箱=[" + dEmail
                            + "] 电话=[" + dPhone + "]\n");
                }
                writer.close();
            } catch (JsonIOException e) {
                e.printStackTrace();
            } catch (JsonSyntaxException e) {
                e.printStackTrace();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
    }
