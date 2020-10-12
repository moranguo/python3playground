def get_multiply(big_a: str, big_b: str):
    # 也可以加上对参数的验证，比如输入的是不是整数字符串
    if big_a == "0" or big_b == "0":
        return "0"

    max_length = len(big_a) + len(big_b)
    result = [0]*max_length
    big_a_ints = [int(i) for i in big_a]
    big_b_ints = [int(i) for i in big_b]

    # 记录当前正在计算的位置，倒序，初始化为0
    curr = 0
    # 记录个位十位，初始化为0
    x, y, z = 0, 0, 0

    i = len(big_b) - 1
    while i >= 0:
        curr = len(big_a) + i   # 实际为 max_length - (len(big_b) - i) 简化得到
        j = len(big_a) - 1
        while j >= 0:
            z = big_b_ints[i] * big_a_ints[j] + result[curr]  # 乘积 并加上 上一次计算的进位
            x = z % 10  # 个位
            y = z // 10  # 十位
            result[curr] = x  # 计算值存到数组result中
            result[curr - 1] += y  # curr-1表示前一位，这里是进位的意思
            curr -= 1
            j -= 1
        i -= 1

    # 最前面的0都不输出
    output_index = 0
    for t in range(max_length):
        if result[t] != 0:
            output_index = t
            break

    output_result_str = []
    for i in range(output_index, max_length):
        output_result_str.append(str(result[i]))

    return "".join(output_result_str)


if __name__ == "__main__":
    assert get_multiply("123456789", "987654321") == "121932631112635269"
    assert get_multiply("12345678987654321", "98765432123456789") == "1219326320073159566072245112635269"
    print("%s * %s = %s" % ("0", "0", get_multiply("0", "0")))
    print("%s * %s = %s" % ("9", "0", get_multiply("9", "0")))
    print("%s * %s = %s" % ("0", "4", get_multiply("0", "4")))
    print("%s * %s = %s" % ("1", "2", get_multiply("1", "2")))
    print("%s * %s = %s" % ("7", "4", get_multiply("7", "4")))
    print("%s * %s = %s" % ("99", "19", get_multiply("99", "19")))
    print("%s * %s = %s" % ("99", "99", get_multiply("99", "99")))
    print("%s * %s = %s" % ("123456789", "987654321", get_multiply("123456789", "987654321")))
    print("%s * %s = %s" % ("12345678987654321", "98765432123456789",
                             get_multiply("12345678987654321", "98765432123456789")))

    # 验证两个大数相乘的结果，将乘法转化为加法，例如(A+1)*B-A*B=B
    # 123456789 * 34 = 4197530826
    # 123456788 * 34 = 4197530792
    print("%s * %s = %s" % ("123456789", "34", get_multiply("123456789", "34")))
    print("%s * %s = %s" % ("123456788", "34", get_multiply("123456788", "34")))


'''
Java版
public class TestMulti {

    public static void main(String[] args) {
        long timeStart = System.currentTimeMillis();
        System.err.println("\nresult=" + getMult("99", "19"));
        System.err.println("\nresult=" + getMult("99", "99"));
        System.err.println("\nresult=" + getMult("123456789", "987654321"));
        System.err.println("\nresult=" + getMult("12345678987654321", "98765432123456789"));
        System.err.println("\ntake time: " + (System.currentTimeMillis() - timeStart));
    }
    
    public static String getMult(String bigIntA, String bigIntB) {
        int maxLength = bigIntA.length() + bigIntB.length();
//      if (maxLength < 10) { // Integer.MAX_VALUE = 2147483647;
//          return String.valueOf(Integer.valueOf(bigIntA) * Integer.valueOf(bigIntB));
//      }
        int[] result = new int[maxLength];
        int[] aInts = new int[bigIntA.length()];
        int[] bInts = new int[bigIntB.length()];

        for (int i = 0; i < bigIntA.length(); i++) {
            aInts[i] = bigIntA.charAt(i) - '0';// bigIntA字符转化为数字存到数组
        }
        for (int i = 0; i < bigIntB.length(); i++) {
            bInts[i] = bigIntB.charAt(i) - '0';// bigIntB字符转化为数字存到数组
        }

        int curr; // 记录当前正在计算的位置，倒序
        int x, y, z; // 记录个位十位

        for (int i = bigIntB.length() - 1; i >= 0; i--) {
            curr = bigIntA.length() + i; // 实际为 maxLength - (bigIntB.length() - i) 简化得到
            for (int j = bigIntA.length() - 1; j >= 0; j--) {
                z = bInts[i] * aInts[j] + result[curr]; // 乘积 并加上 上一次计算的进位
                x = z % 10;// 个位
                y = z / 10;// 十位
                result[curr] = x; // 计算值存到数组c中
                result[curr - 1] += y; // curr-1表示前一位，这里是进位的意思
                curr--;
            }
        }

        int t = 0;
        for (; t < maxLength; t++) {
            if (result[t] != 0) {
                break; // 最前面的0都不输出
            }
        }
        StringBuilder builder = new StringBuilder();
        if (t == maxLength) { // 结果为0时
            builder.append('0');
        } else { // 结果不为0
            for (int i = t; i < maxLength; i++) {
                builder.append(result[i]);
            }
        }
        return builder.toString();
    }
}

'''