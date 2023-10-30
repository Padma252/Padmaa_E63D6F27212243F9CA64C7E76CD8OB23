public interface IInnings 
{
    IPlayer Batsman { get;  }
    IPlayer Bowler { get; }
    int TotalScore { get; }
    List<int> ScoreByEachThrow { get;}
    void AddScore(int score);
}

class Innings : IInnings
{
    public IPlayer Batsman
    {
get;
        private set;
    }

    public IPlayer Bowler
    {
        get;
        private set;
    }

    public int TotalScore
    {
        get;
        private set;
    }

    public Innings(IPlayer batsman, IPlayer bowler)
    {
        Batsman = batsman;
        Bowler = bowler;
        ScoreByEachThrow = new List<int>();
{
        get;
        private set;
    }

    public void AddScore(int score)
    {
        ScoreByEachThrow.Add(score);
        TotalScore += score;
    }
}