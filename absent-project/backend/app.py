import matplotlib.pyplot as plt



def weekly_attendance(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Attendance Count'], marker='o')
    plt.title('Weekly Attendance Visualization')
    plt.xlabel('Date')
    plt.ylabel('Attendance Count')
    plt.grid(True)
    plt.show()