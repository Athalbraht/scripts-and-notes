real function sigmoid(x)
      real :: x
      sigmoid = 1/(1+exp(-x))
      return
end function sigmoid

real function dsigmoid(x)
        real :: x
        real :: sigmoid
        dsigmoid = sigmoid(x)*(1-sigmoid(x))
        return
end function dsigmoid

subroutine learn(x, y, w, n)
        integer :: n, i,j
        real :: error, res, ssum
        real, dimension(0:1,2) :: x
        real, dimension(0:2) :: y
        real, dimension(0:1), intent(inout) :: w
        do i=0, n
                print *, 'Learning::', w
                do j=0, size(y)
                        call rresult(x(:,j), w, res, ssum) 
                        error = y(j) - res
                        do k=0, size(w)
                                w(k) = w(k) + error*res*dsigmoid(ssum)
                        end do

                end do
        end do

end subroutine learn

subroutine rresult(x, w, r,s)
        implicit none
        real :: ssum=0
        real, intent(out) :: r,s
        real :: sigmoid
        real, dimension(0:1) :: x, w
        integer :: i=0
        do i=0, size(w)
                ssum = ssum + w(i)*x(i)
        end do
        ssum = ssum+1
        s = ssum
        r = sigmoid(ssum)
end subroutine rresult

subroutine get_data(x, y)
       implicit none 
       real, dimension(0:1,0:2),intent(out) :: x
       real, dimension(0:2), intent(out) :: y
       x(0,0) = 1 
       x(1,0) = 0 
       x(0,1) = 0 
       x(1,1) = 1 
       x(0,2) = 1 
       x(1,2) = 1 
       y(0) = 0 
       y(1) = 0 
       y(2) = 1 
end subroutine get_data

program perceptron
      implicit none
      real, dimension(0:1,0:2) :: x_t
      real, dimension(0:2) :: y_t
 
      real, dimension(0:1) :: input
      real :: output, s
      real, dimension(0:1) :: weights
      
      input(0) = 1
      input(1) = 1
      weights(0) = -0.242
      weights(1) = 0.42
      read(*,*) input(0)
      read(*,*) input(1)
      call rresult(input, weights, output, s)
      print *, 'result::', output
      print *, 'weights::',weights(0), weights(1) 
      call get_data(x_t, y_t)
      call learn(x_t, y_t, weights, 100)
      print *, 'weights::',weights(0), weights(1) 
      do
         read(*,*) input(0)
         read(*,*) input(1)
         call rresult(input, weights, output, s)
         print *, 'result::', output , s, input      
      end do
end program perceptron
