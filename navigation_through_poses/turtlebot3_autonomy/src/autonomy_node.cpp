#include "autonomy_node.h"


using namespace std::chrono_literals;

const std::string bt_design_dir =
    ament_index_cpp::get_package_share_directory("turtlebot3_autonomy") + "/bt_design";

AutonomyNode::AutonomyNode(const std::string &nodeName) : Node(nodeName)
{
  RCLCPP_INFO(get_logger(),"Init done");
  this->declare_parameter<std::string>("location_file");

  // Optionally retrieve and log the value (for debug/logging)
  std::string location_file;
  this->get_parameter("location_file", location_file);
  RCLCPP_INFO(get_logger(), "Loaded location_file: %s", location_file.c_str());
}

void AutonomyNode::setup()
{  
  RCLCPP_INFO(get_logger(),"Setting up");
  create_behavior_tree();
  RCLCPP_INFO(get_logger(),"BT created");

  const auto timer_period = 500ms;
  timer_ = this->create_wall_timer(
	timer_period,
	std::bind(&AutonomyNode::update_behavior_tree,this));
  rclcpp::spin(shared_from_this());
  rclcpp::shutdown();

}

void AutonomyNode::create_behavior_tree()
{
  BT::BehaviorTreeFactory factory;


  BT::NodeBuilder builder =
      [=](const std::string &name, const BT::NodeConfiguration &config)
  {
    return std::make_unique<GoToPose>(name, config, shared_from_this());
  }; //node builder is used when no. of argumnentsare greater than two-name,config,node pointer

  factory.registerBuilder<GoToPose>("GoToPose", builder);

  RCLCPP_INFO(get_logger(), bt_design_dir.c_str());

  tree_ = factory.createTreeFromFile(bt_design_dir + "/tree.xml");
  RCLCPP_INFO(get_logger(), "3");
}
void AutonomyNode::update_behavior_tree()
{
  BT::NodeStatus tree_status = tree_.tickRoot();

  if (tree_status == BT::NodeStatus::RUNNING)
  {
    return;
  }
  else if (tree_status == BT::NodeStatus::SUCCESS)
  {
    RCLCPP_INFO(this->get_logger(), "Finished Navigation");
  }
  else if (tree_status == BT::NodeStatus::FAILURE)
  {
    RCLCPP_INFO(this->get_logger(), "Navigation Failed");
    timer_->cancel();
  }

}

int main(int argc,char **argv)
{
  rclcpp::init(argc,argv);
  auto node = std::make_shared<AutonomyNode>("autonomy_node");
  node->setup();

  rclcpp::spin(node);
  rclcpp::shutdown();

}
