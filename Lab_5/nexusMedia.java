package Lab_5;

public abstract class nexusMedia{

    protected double fileSize;
    protected String title;

    public nexusMedia(double fileSize, String title){
        this.fileSize = fileSize;
        this.title = title;
        
    }

    public abstract void play();

}


