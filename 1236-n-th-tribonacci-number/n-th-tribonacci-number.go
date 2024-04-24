func tribonacci(n int) int {
    var counter int = 3
    var a int = 0
    var b int = 1
    var c int  = 1

    if n ==0{
        return 0
    }
    if n==1{
        return 1
    }

    if n==2{
        return 1
    }
    if n==3{
        return 2
    }
    for counter<=n{
        var d int = a+b+c
        fmt.Println(d)
        a = b
        b=c
        c=d
        counter +=1
    }
    return c
    
}