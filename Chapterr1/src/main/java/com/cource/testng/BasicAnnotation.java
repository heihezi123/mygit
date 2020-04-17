package com.cource.testng;

import org.testng.annotations.*;

public class BasicAnnotation {
    @Test
    public void testCase1(){
        System.out.println("这是测试用例1");
    }
    @Test
    public void testCase2(){
        System.out.println("这是测试用例2");
    }
    @BeforeMethod
    public void beforeMethod(){
        System.out.println("这是的测试之前运行的");
    }
    @AfterMethod
    public void AfterMethod(){
        System.out.println("这是的测试之后运行的");
    }
    @BeforeClass
    public void beforeClass(){
        System.out.println("这是在类之前运行的");
    }
    @AfterClass
    public void Class(){
        System.out.println("这是在类之后运行的");
    }
    @BeforeSuite
    public void beforeSuite(){
        System.out.println("这是beforeSuite测试套件");
    }
    @AfterSuite
    public void afterSuite(){
        System.out.println("这是afterSuite测试套件");
    }
}
