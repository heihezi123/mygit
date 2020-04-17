package com.cource.testng;

import org.testng.annotations.*;

public class SuiteConfig {
    @BeforeSuite
    public  void beforeSuit(){
        System.out.println("before suite运行拉");
    }
    @AfterSuite
    public  void afterSuit(){
        System.out.println("after suite运行拉");
    }
    @BeforeTest
    public  void beforeTest(){
        System.out.println("beforetest");
    }
    @AfterTest
    public  void afterTest(){
        System.out.println("aftertest");
    }
}
