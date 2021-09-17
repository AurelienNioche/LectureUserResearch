
T = readtable("mt_cars.csv");

scatter(T.wt, T.mpg);
xlabel("Weight");
ylabel("Milage");

print('cars_matlab','-dpng', '-r400')