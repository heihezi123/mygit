package com.course.httpclient.cookies;

import org.apache.http.HttpResponse;
import org.apache.http.ParseException;
import org.apache.http.client.CookieStore;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.cookie.Cookie;
import org.apache.http.impl.client.BasicCookieStore;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.jsoup.Connection;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import java.io.IOException;
import java.util.List;
import java.util.Locale;
import java.util.ResourceBundle;

public class MyCookiesForGet {

    private String url;
    private ResourceBundle bundle;
    private CookieStore store;

    @BeforeTest
    public void beforeTest() {
        bundle = ResourceBundle.getBundle("application", Locale.CHINA);
        url = bundle.getString("test.url");
    }

    @Test
    public void testGetCookies()  {
        String result;
        // 获取文件 拼接
        String uri = bundle.getString("getCookies.uri");
        String getTestUrl = this.url + uri;

        try {
            BasicCookieStore cookieStore = new BasicCookieStore();
            // 获取 响应
            HttpGet get = new HttpGet(getTestUrl);
            CloseableHttpClient httpClient = HttpClients.custom().setDefaultCookieStore(cookieStore).build();
//            CloseableHttpClient build = HttpClientBuilder.create().build();
//            CloseableHttpResponse execute = build.execute(get);
            CloseableHttpResponse execute = httpClient.execute(get);
            result = EntityUtils.toString(execute.getEntity(), "utf-8");
            System.out.println(result);

            // 获取cookies信息

            List<Cookie> cookies = cookieStore.getCookies();
            for (Cookie cookie : cookies) {
                String name = cookie.getName();
                String value = cookie.getValue();
                System.out.println("cookies: key= " + name + "  value= " + value);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }

    }
    @Test(dependsOnMethods ={"testGetCookies"})
    public  void testGetWithCookies() throws IOException {
        String uri = bundle.getString("test.get.with.cookies");
        String getTestUrl = this.url + uri;
        HttpGet get = new HttpGet(getTestUrl);
        BasicCookieStore cookieStore = new BasicCookieStore();
        CloseableHttpClient httpClient = HttpClients.custom().setDefaultCookieStore(cookieStore).build()

        //设置COOKIES信息
        httpClient.(this.store);
        HttpResponse response= client.execute(get);
        //获取响应的状态码
        int statusCode = response.getStatusLine().getStatusCode();
        System.out.println("statusCode="+statusCode);

        if(statusCode ==200){
            String result = EntityUtils.toString(response.getEntity(), "utf-8");
            System.out.println(result);
        }

    }
}

