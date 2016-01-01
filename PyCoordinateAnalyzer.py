import matplotlib.pyplot as plt

# read input file
f = open('input.csv', 'r')
input_data = f.readlines()

input_num_of_day_str = input_data[0][:-1].split(',')
input_num_of_user_str = input_data[1][:-1].split(',')

# generate list of float type
input_num_of_day_f = []
input_num_of_user_f = []

for i in range (0, len(input_num_of_day_str)):
    input_num_of_day_f.append(float(input_num_of_day_str[i]))
    input_num_of_user_f.append(float(input_num_of_user_str[i]))

print('input_num_of_day_f:')
print(input_num_of_day_f)
print('input_num_of_user_f:')
print(input_num_of_user_f)

# calculate number of cumulative user
num_of_cumulative_user = [input_num_of_user_f[0]]
for i in range (1, len(input_num_of_day_str)):
    num_of_cumulative_user.append(num_of_cumulative_user[i - 1] + float(input_num_of_user_f[i]))
print('num_of_cumulative_user:')
print(num_of_cumulative_user)

#calculate sum
total_sum = 0.0
for i in input_num_of_user_f:
    total_sum += float(i)

#calculate avg
total_avg = round(total_sum / input_num_of_day_f.__len__(), 3)
print('total_sum: ' + str(total_sum))
print('total_avg: ' + str(total_avg))

# draw window
plt.title('DAU')
plt.ylabel('millions')
plt.xlabel('days')
plt.plot(input_num_of_day_f, input_num_of_user_f)
plt.plot(input_num_of_day_f, num_of_cumulative_user)
plt.axis([0, 21, 0, 66])
plt.text(13, 27, 'Daily AVG user: ' + str(total_avg))
plt.text(13, 23, 'Total Cumulative Count of Users: ' + str(total_sum))
plt.text(13, 57, 'Cumulative user count')
plt.text(7, 8, 'Daily user connection')
plt.grid(True)

plt.show()
