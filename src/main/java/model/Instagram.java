package model;

public class Instagram {

    public String username;
    public String password;

    public int nFollowing;
    public int nFollowers;

    public Instagram(String user, String passw) {
        init(user,passw);
    }

    public void init(String user, String passw){
        this.username = user;
        this.password = passw;
    }

}
