// Only doing part 2 in zig

const std = @import("std");

const data = @embedFile("day1.txt");

pub fn main() !void {
    var ret: usize = 0;
    var iter = std.mem.splitScalar(u8, data, '\n');
    while (iter.next()) |line| {
        ret += findFirstDigit(line) * 10 + findLastDigit(line);
    }
    const stdout = std.io.getStdOut().writer();
    try stdout.print("{}", .{ret});
}

const digits = [_][]const u8{
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
};

// kindof wanna implement aho-corasick for future zig stuff,
// but std.mem.lastIndexOf(Any) std.mem.indexOf(Any)
// are actually pretty cool
fn findFirstDigit(line: []const u8) usize {
    var min_idx: usize = std.math.maxInt(usize);
    var digit: usize = 0;
    for (digits, 1..) |dig, i| {
        if (std.mem.indexOf(u8, line, dig)) |idx| {
            if (min_idx >= idx) {
                min_idx = idx;
                digit = i;
            }
        }
    }
    if (std.mem.indexOfAny(u8, line, "123456789")) |first_dig| {
        if (min_idx >= first_dig) {
            min_idx = first_dig;
            digit = line[first_dig] - '0';
        }
    }
    return digit;
}
fn findLastDigit(line: []const u8) usize {
    var max_idx: usize = 0;
    var digit: usize = 0;
    for (digits, 1..) |dig, i| {
        if (std.mem.lastIndexOf(u8, line, dig)) |idx| {
            if (max_idx <= idx) {
                max_idx = idx;
                digit = i;
            }
        }
    }
    if (std.mem.lastIndexOfAny(u8, line, "123456789")) |last_dig| {
        if (max_idx <= last_dig) {
            max_idx = last_dig;
            digit = line[last_dig] - '0';
        }
    }
    return digit;
}
