package demo

import org.junit.Assert
import org.junit.Test

class TestPerson{
    @Test
    fun testOutput(){
        val p = Person("sidharth", 32)
        Assert.assertEquals(p.sayMyName(), "Mera nam sidharth hai")
    }
}