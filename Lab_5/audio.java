package Lab_5;

public class audio extends nexusMedia {
    protected String sampleRate;

    public audio(double fileSize, String title, String sampleRate){
        super(fileSize, title);

        this.sampleRate = sampleRate; 

    }

    @Override 
    public void play(){
        System.out.println("Outputting sound at " + this.sampleRate);
        
    }
}
