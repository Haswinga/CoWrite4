from crewai import Task

def create_content(agent, content_prompt):
  return Task(
      description=f"Create engaging content based on the prompt: {content_prompt}",
      expected_output="A social media post including text and visuals",
      agent=agent,
  )

def manage_content_calendar(agent):
  return Task(
      description="Manage the content calendar (add, update, remove content items)",
      expected_output="An updated content calendar",
      agent=agent,
  )

def schedule_social_media_posts(agent):