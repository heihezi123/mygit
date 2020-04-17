package com.cource.testng;

import org.testng.annotations.Test;

public class IgnoreTest {
    @Test
    public  void ignor1(){
        System.out.println("ignore1 执行");
    }
    @Test(enabled = false)
    public  void ignor2(){
        System.out.println("ignore2 执行");
    }
    @Test(enabled = true)
    public  void ignor3(){
        System.out.println("ignore3 执行");
    }
}
