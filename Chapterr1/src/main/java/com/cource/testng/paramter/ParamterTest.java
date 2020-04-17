package com.cource.testng.paramter;

import org.testng.annotations.Test;
import org.testng.annotations.Parameters;

public class ParamterTest {
    @Test
    @Parameters({"name","age"})
    public  void paramTest1(String name,int age){
        System.out.println("name =" + name +";| age =" + age);
    }
}
