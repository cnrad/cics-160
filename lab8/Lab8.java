class Lab8 {
    public static void main(String[] args){
        String s1 = "Jaime";
        String s2 = "Jaime";
        System.out.println("are s1 and s2 the same string? " + (s1==s2));
    }

    public static boolean checkReply(String s, char c) {
        Character lowercased = s.charAt(0);
        return lowercased.equals(c);
    }
}
