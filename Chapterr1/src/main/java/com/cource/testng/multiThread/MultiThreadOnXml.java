package com.cource.testng.multiThread;

import org.testng.annotations.Test;

public class MultiThreadOnXml {
    @Test
    public void test1() {
        //System.out.println(1);
        System.out.printf("Thrad Id : %s%n",Thread.currentThread().getId());
    }

    @Test
    public void test2() {
        //System.out.println(1);
        System.out.printf("Thrad Id : %s%n",Thread.currentThread().getId());
    }

    @Test
    public void test3() {
        //System.out.println(1);
        System.out.printf("Thrad Id : %s%n",Thread.currentThread().getId());
    }

}
