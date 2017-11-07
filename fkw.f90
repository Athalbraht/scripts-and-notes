function delta(a,b,c)

    real :: a, b, c
    delta = b**2. - 4.*a*c
    return

end function delta  


subroutine get_data(a,b,c)

    real :: a,b,c
    write(*,*) 'a'
    read(*,*) a
    write(*,*) 'b'
    read(*,*) b
    write(*,*) 'c'
    read(*,*) c

end subroutine get_data


subroutine check(a,b,c)

    real :: a,b,c,d
    real :: delta
    d = delta(a,b,c)

    if (d == 0) then
        print *, 'x=', -b/(2*a)
    else if (d > 0) then
        print *, "x1=", (-b - sqrt(d))/(2*a)
        print *, "x2=", (-b + sqrt(d))/(2*a)
    else
        print *, 'brak'
    end if

end subroutine check
        

program main

    implicit none
    real :: a, b, c,d
    call get_data(a,b,c)
    call check(a,b,c)

end program main     
