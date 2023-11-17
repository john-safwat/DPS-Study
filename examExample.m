% define the time and amplitude of the signal 

time = -2:6 ;
amblitude = [0,0,2,3,2,1,0,0,0];

% Define the figure to display plots in 
figure("Name", "Siganl Operation" , "NumberTitle","off")


% define subplots 
% define the subplot using subplot function subplot( Number of Rows ,
% Numebr of Columns , Subplot Index ) in screen Grid View 
subplot( 3 , 2 , 1 )

% pass plot paramiters signal time and amblitude 
stem(time , amblitude)

% title of graph 
title("Original Signal")
xlabel("Time")
ylabel("Amblitude")


% 1/2n plotting
subplot( 3 , 2 , 2 )

signalOneTime = time * 2;

% pass plot paramiters signal time and amblitude 
stem(signalOneTime , amblitude)

% title of graph 
title("1/2 n")
xlabel("Time")
ylabel("Amblitude")


% 3x(1/2n) plotting
subplot( 3 , 2 , 3 )

signalOneAmplitude = amblitude * 3;

% pass plot paramiters signal time and amblitude 
stem(signalOneTime , signalOneAmplitude)

% title of graph 
title("3x(1/2n)")
xlabel("Time")
ylabel("Amblitude")

% (1-n) plotting
subplot( 3 , 2 , 4 )

signalTwoTime = -(time -1);

% pass plot paramiters signal time and amblitude 
stem(signalTwoTime , amblitude)

% title of graph 
title("(1-n)")
xlabel("Time")
ylabel("Amblitude")

% 0.5x(1-n) plotting
subplot( 3 , 2 , 5 )

signalTwoAmblitude = amblitude * 0.5;

% pass plot paramiters signal time and amblitude 
stem(signalTwoTime , signalTwoAmblitude)

% title of graph 
title("0.5x(1-n)")
xlabel("Time")
ylabel("Amblitude")

% 0.5x(1-n) plotting
subplot( 3 , 2 , 6 )

amblitude = signalTwoAmblitude + signalOneAmplitude;

% pass plot paramiters signal time and amblitude 
stem(time , amblitude)

% title of graph 
title("0.5x(1-n)")
xlabel("Time")
ylabel("Amblitude")



